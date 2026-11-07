# Lab 02 — Problem Scan & Quick Problem Cards

**Đề tài chọn:** Hỗ trợ tìm người thất lạc tại Vinpearl / VinWonders bằng Person Re-identification (Re-ID).

Nguồn đầu vào: [ProblemStatement.md](references/ProblemStatement.md), worksheet và student guide của lab. Đây là bài scoping dựa trên tình huống đề bài; chưa phỏng vấn nhân viên, chưa tiếp cận NVR hoặc đo số liệu tại doanh nghiệp. Các thời gian ngoài con số 30–60 phút trong đề là giả định để thiết kế PoC, không phải thống kê vận hành.

## Phase 1 — SCAN

| # | Đơn vị trong tình huống lab | Lens | Bài toán cụ thể / đầu ra mong muốn |
|---|---|---|---|
| 1 | Vinpearl / VinWonders | Tốn thời gian | Bảo vệ phải tua camera tìm trẻ thất lạc; cần danh sách clip ứng viên có camera, thời điểm và ảnh đối chiếu. |
| 2 | Vinpearl / VinWonders | Pain từ người khác | Phụ huynh hoảng loạn, thông tin báo lạc thiếu; cần biểu mẫu tiếp nhận có người phụ trách và cơ chế hỏi bổ sung. |
| 3 | Vinhomes | Lặp lại | Nhân viên phân loại phản ánh cư dân rồi chuyển bộ phận; cần nháp phân loại và tuyến xử lý, có người duyệt. |
| 4 | Xanh SM | AI-upgrade | Điều phối viên tổng hợp pin, vị trí và yêu cầu tài xế để soạn hướng dẫn; cần nháp dựa trên dữ liệu trạm đã xác thực. |
| 5 | VinFast | Lặp lại | Đối chiếu hóa đơn sạc với nhật ký giao dịch; cần bảng chênh lệch có mã giao dịch, dùng rule trước khi cân nhắc AI. |
| 6 | Vinpearl | Pain từ người khác | Quản lý đọc nhiều phản hồi dịch vụ; cần gom nhóm vấn đề và dẫn lại review nguồn để ưu tiên xử lý. |

Danh sách sử dụng đủ 4 lenses. Các cơ hội #2–#6 là giả thuyết cần khảo sát, không khẳng định doanh nghiệp đang có lỗi hay tổn thất cụ thể.

## Phase 2 — QUICK-ASSESS

### Card #1 — Tìm người thất lạc qua camera

| Trường | Nội dung |
|---|---|
| Công ty | Vinpearl / VinWonders |
| Actor / Operator | Phụ huynh và người thất lạc chịu tác động; CSKH tiếp nhận; Control Room rà camera; tuần tra xác minh hiện trường. |
| Workflow hiện tại | 1. Nhận báo lạc và ảnh → 2. Bàn giao cho Control Room → 3. Chọn camera/khoảng giờ → 4. Tua và so sánh bằng mắt → 5. Báo vị trí nghi vấn để tuần tra xác minh. |
| Bottleneck | Bước 4: đề bài nêu mất 30–60 phút rà camera. Ảnh khác góc và trang phục tương tự làm tăng ứng viên nhầm. |
| AI hỗ trợ | Detector / tracker tạo tracklet, encoder Re-ID xếp hạng ứng viên; UI hiển thị clip nguồn. Nhân viên duyệt, AI không xác nhận danh tính. |
| Metric có số | Mục tiêu PoC: p95 thời gian từ ảnh hợp lệ đến danh sách ứng viên <180 giây cho cửa sổ 2 giờ đã xác định cấu hình; Top-5 hit rate >90%; search recall >85%. Chưa đo đạt. |
| Quick Architecture | **Rule/state-machine + Computer Vision Re-ID**; LLM chỉ là tính năng phụ định dạng metadata, không xử lý so khớp người. Không cần agent tự trị. |
| Boundary / Fallback | Yêu cầu chính thức từ người giám hộ và duyệt An ninh; giữ người duyệt trước điều phối; ảnh kém/không có ứng viên thì rà thủ công và xin ảnh tốt hơn. |

### Card #3 — Phân loại phản ánh cư dân

| Trường | Nội dung |
|---|---|
| Công ty | Vinhomes |
| Actor / Operator | Cư dân chờ hỗ trợ; CSKH phân loại; đội kỹ thuật nhận việc. |
| Workflow hiện tại | 1. Nhận phản ánh → 2. Đọc và hỏi thêm → 3. Chọn nhóm lỗi → 4. Chuyển đơn vị → 5. Theo dõi phản hồi. |
| Bottleneck | Đọc và chuyển nhóm với nội dung không có cấu trúc. Giả định 5 phút/phiếu để lập kế hoạch đo baseline. |
| AI hỗ trợ | LLM đề xuất loại vấn đề từ danh mục đã định nghĩa; rule ưu tiên sự cố khẩn; nhân viên duyệt. |
| Metric có số | Mục tiêu đề xuất: median thời gian phân loại ≤1 phút/phiếu; ≥90% nháp được duyệt không sửa nhóm trên tập test đã gán nhãn. |
| Quick Architecture | Rule router cho nhóm rõ ràng; LLM feature cho văn bản mơ hồ. |
| Boundary / Fallback | Không tự quyết tranh chấp, phí hoặc quyền cư dân; không tự đóng ticket; thiếu thông tin thì hỏi lại hoặc chuyển CSKH. |

### Card #4 — Nháp hướng dẫn sự cố pin

| Trường | Nội dung |
|---|---|
| Công ty | Xanh SM |
| Actor / Operator | Tài xế và điều phối viên. |
| Workflow hiện tại | 1. Nhận cuộc gọi → 2. Xác minh pin/vị trí → 3. Tra trạm/cứu hộ → 4. Soạn hướng dẫn → 5. Duyệt và gửi. |
| Bottleneck | Tra cứu và soạn nháp. Giả định 10 phút/lượt; cần đo trước khi dùng làm baseline. |
| AI hỗ trợ | Rule kiểm tra an toàn từ telemetry; LLM soạn nháp từ thông tin đã xác minh. |
| Metric có số | Mục tiêu đề xuất: thời gian soạn nháp ≤2 phút; 100% nháp qua rule pin và duyệt người trong tập boundary test. |
| Quick Architecture | Rule + LLM feature, không agent tự điều xe. |
| Boundary / Fallback | Giữ `[DRAFT_ONLY]`; pin <5% và trạm >5km thì đề xuất xe sạc di động dạng nháp; dữ liệu thiếu thì hỏi lại. Đây là quy tắc bài lab, không phải hướng dẫn vận hành xe thực tế. |

## Lựa chọn và đánh đổi

Chọn **Card #1** để phân tích sâu vì trực tiếp bám `ProblemStatement.md`: có người vận hành, đầu ra và điểm nghẽn rõ. Giá trị trước mắt là rút ngắn rà video để nhân viên ra quyết định, không phải tự động theo dõi mọi khách.

Card #3 dễ tạo prototype văn bản nhưng cần nhãn ticket và routing directory chưa được cung cấp. Card #4 phù hợp starter code nên vẫn được hoàn thiện riêng làm bài code cá nhân; không thay thế đề tài Re-ID. Quyết định đề tài ở đây là đề xuất của bài làm, chưa phải biên bản họp hay phê duyệt thực tế của nhóm/doanh nghiệp.

Xem [Deep-dive](02-deep-dive-report.md), [AI log](03-ai-log.md) và [hướng dẫn chạy/nộp](SUBMISSION.md).
