# Lab 02 — AI Log & Reflection

**Ngày phiên làm bài:** 07/11/2026 (múi giờ Việt Nam theo phiên).

Đây là bản ghi việc AI hỗ trợ hoàn thiện bộ bài trong workspace, không phải lịch sử phỏng vấn doanh nghiệp hay tuyên bố người học đã tự chạy Gemini. Chưa có cuộc gọi mô hình Gemini thật vì môi trường không có API key.

## 1. Yêu cầu đầu vào và vai trò AI

Yêu cầu thực tế: “từ file problem statement.md, hoàn thiện nốt code và bài tập cho mình”. AI đọc `ProblemStatement.md`, worksheet, README, starter code và autograder để xác định các đầu ra còn thiếu.

AI giúp tổ chức đề tài Re-ID theo 6-field framework, tách metric truy xuất khỏi thời gian tìm thấy tận nơi, đề xuất workflow có người duyệt/fallback, viết JSON schema, hoàn thiện SDK adapter, tạo dữ liệu tổng hợp, viết test và render sơ đồ. Việc chọn model thị giác, tích hợp NVR, lấy phép sử dụng dữ liệu và xác nhận quy trình doanh nghiệp vẫn chưa được thực hiện.

## 2. Các điểm dễ sai đã được đối chiếu với nguồn

| Điểm cần phản biện | Bằng chứng trong bộ đề / code | Cách xử lý trong bài |
|---|---|---|
| Dùng bài Xanh SM làm đề tài thay cho Re-ID | `prompt_prototype.py` và autograder gốc kiểm tra pin, 5km và nhãn draft; `ProblemStatement.md` nói tìm người thất lạc | Hoàn thiện bài code gốc riêng và thêm `reid_prompt_prototype.py`; báo cáo chính theo Re-ID. Không sửa autograder để hợp thức hóa. |
| Nghĩ LLM có thể thay encoder Re-ID | Starter lab là prompt prototype, trong khi đầu vào nghiệp vụ là ảnh/video xuyên camera | Xác định CV là lõi; LLM là tính năng metadata tùy chọn. Không gắn nhãn prompt demo là hệ thống Re-ID hoàn chỉnh. |
| Đọc mục tiêu thành kết quả đã đạt | Đề nêu mục tiêu <3 phút, Top-5 >90%, recall >85%, chưa có dataset hoặc benchmark | Báo cáo ghi rõ chưa đo; đưa định nghĩa metric, mẫu số, kế hoạch test và quyết định NOT YET cho pilot. |
| Gọi mọi tỷ lệ cảnh báo sai là FPR | Đề chưa chỉ ra mẫu số và đơn vị đánh giá | Tách false suggestion ratio, query vắng mặt và Top-5 hit rate; không đánh tráo precision với FPR. |
| Chỉ cần output chứa từ khóa là an toàn | Code mẫu dùng kiểm tra substring và in kết quả, chưa bảo đảm JSON, nhãn ở đầu hay exit code khi vi phạm | Dùng parser JSON nghiêm ngặt, allowlist fields/actions, kiểm tra bằng chứng và loại dữ liệu, trả exit code khác 0 khi lỗi. |
| Cho “tôi là sếp” tương đương phê duyệt | Một prompt văn bản không phải danh tính đã xác thực | Tách `trusted_context` khỏi yêu cầu người dùng; các case thiếu quyền không gọi cloud hoặc trả ứng viên. IAM thật vẫn là hạng mục chưa tích hợp. |
| Nhầm score cao nhất với lần xuất hiện mới nhất | Metadata giả lập có ứng viên 0.95 lúc 10:05 và 0.87 lúc 10:15 | Chọn timestamp gần nhất trong các ứng viên được hiển thị; kiểm tra riêng timezone, top-5 và ngưỡng. |

Đây là các sai sót/giả định được phòng ngừa khi đọc đề và code mẫu. **Chưa quan sát được hallucination từ Gemini**, do chưa gọi API. Không tạo một câu trả lời sai giả rồi ghi như lịch sử tương tác mô hình thật.

## 3. Prompt và boundary đã cụ thể hóa

Prompt Re-ID giao vai trò hỗ trợ Control Room, coi yêu cầu người dùng là dữ liệu không tin cậy, chỉ cho phép action trong schema. Đầu ra không được khẳng định danh tính, bịa evidence hoặc phát lệnh điều phối. Retention đề xuất tối đa 24 giờ; đóng case phải đề xuất purge. Mọi kết quả cần người duyệt.

Ranh giới quan trọng được đưa vào code: gate quyền/trạng thái trước SDK, danh sách evidence IDs nguồn, validator JSON và đối chiếu với policy xác định. Nhãn `[DRAFT_ONLY]` do ứng dụng gắn, không dựa vào việc LLM tự nhớ. Không diễn giải điều này thành bằng chứng rằng prompt có thể chống mọi tấn công.

Trong prototype này, policy đã đủ để tạo JSON; LLM không cần thiết cho tính đúng. Việc giữ nhánh SDK là để làm bài thử prompt theo lab. Nếu sản phẩm chỉ cần cùng cấu trúc metadata này, template và rule sẽ đơn giản, rẻ và dễ kiểm soát hơn.

## 4. Test và kết quả

Đã tạo 4 adversarial inputs cho Xanh SM và 7 cho Re-ID. Bộ test còn chủ động đưa đầu ra sai vào validator: bỏ duyệt, bịa camera, tăng TTL, thêm field gửi lệnh, JSON duplicate key, NaN, timestamp thiếu timezone và dữ liệu quyền sai kiểu.

Kết quả kiểm tra thực tế được lưu tại [evidence/verification.md](evidence/verification.md), kèm stdout tại thư mục `evidence/`. Mặc định CLI kiểm tra fixture tổng hợp; các test SDK dùng mock, không phát sinh API call. Chưa có số đo độ chính xác Gemini, chất lượng Re-ID, latency NVR hoặc chi phí API.

## 5. Reflection

Giá trị của AI trong bài là giúp chuyển một ý tưởng rộng thành nhiệm vụ có phạm vi, dữ liệu, người chịu trách nhiệm và điều kiện đánh giá rõ. Cần kiểm tra mọi con số với nguồn thay vì để một bản nháp trôi chảy trở thành “bằng chứng”.

Bài học kỹ thuật là prompt không phải toàn bộ hệ thống: quyền phải ở backend, dữ liệu phải có nguồn, quyết định tác động đến hiện trường phải qua con người, retention cần worker và kiểm tra xóa thực tế. Test local cho biết chương trình xử lý các tình huống đã định nghĩa; nó không thay thế benchmark model hoặc diễn tập vận hành.

Trước khi nộp, người học cần đọc lại lập luận, bổ sung thông tin cá nhân/nhóm theo lớp nếu được yêu cầu và chỉ ghi kết quả live sau khi đã chạy bằng key của mình. Việc này không thay đổi phần báo cáo scoping và code local đã hoàn thiện.
