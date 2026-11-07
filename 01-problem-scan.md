# Problem Scan — Vin Smart Future

Bài làm theo tình huống học tập trong đề, không xác nhận thông tin tổ chức hay vận hành của doanh nghiệp. Tất cả thời gian, lưu lượng và mục tiêu bên dưới là **giả định để thiết kế pilot**, chưa phải thống kê thực tế. Không sử dụng dữ liệu cá nhân thật.

## Phase 1 — SCAN (Cá nhân, 20 phút)

### 4 Lenses tìm bài toán

1. **Lặp lại (Repetitive):** Công việc thực hiện nhiều lần mỗi ngày, có thao tác hoặc quy tắc tương tự nhau.
2. **Tốn thời gian (Time-consuming):** Công việc phải đọc, tra cứu, nhập lại hoặc tổng hợp thông tin thủ công.
3. **AI có thể tốt hơn (AI-upgrade):** Công việc cần hiểu ngôn ngữ tự nhiên, phân loại nội dung hoặc soạn phản hồi phù hợp ngữ cảnh.
4. **Pain từ người khác (Stakeholder Pain):** Điểm nghẽn khiến khách hàng, nhân viên hoặc người vận hành phải chờ, làm lại hay trao đổi nhiều lần.

### List bài toán của tôi

Các bài toán dưới đây là cơ hội khảo sát theo bối cảnh đề bài; chưa có phỏng vấn hoặc log xác nhận tần suất và mức độ tổn thất.

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | VinFast | Lặp lại (Repetitive) | Kế toán đối soát hóa đơn sạc với dữ liệu phiên sạc, kiểm tra mã giao dịch, điện năng và số tiền. Hóa đơn thiếu mã hoặc lệch số liệu phải tra cứu và xử lý thủ công. |
| 2 | Xanh SM | Tốn thời gian (Time-consuming) | Điều phối viên đọc tin nhắn tài xế báo pin yếu, xác minh vị trí và tình trạng xe rồi tra cứu, soạn phương án hỗ trợ. Việc chuyển giữa chat và dữ liệu xe kéo dài thời gian chờ của tài xế. |
| 3 | Vinhomes | AI có thể tốt hơn (AI-upgrade) | Phản ánh cư dân được viết bằng ngôn ngữ tự do, có thể thiếu số tòa hoặc loại sự cố. Nhân viên phải đọc, hỏi lại và phân loại trước khi chuyển đúng bộ phận xử lý. |
| 4 | Vinpearl | Tốn thời gian (Time-consuming) | Nhân viên đọc email đặt phòng đoàn, trích ngày lưu trú, số khách và yêu cầu đặc biệt rồi nhập lại vào hệ thống. Email thay đổi nhiều lần làm tăng nguy cơ bỏ sót hoặc nhập sai thông tin. |
| 5 | Xanh SM | Pain từ người khác (Stakeholder Pain) | Điểm đón trên bản đồ có thể khác nơi khách đang đứng tại chung cư hoặc trung tâm thương mại nhiều cổng. Khách và tài xế phải gọi lại để xác định điểm gặp, kéo dài thời gian đón và có thể dẫn đến hủy chuyến. |

### Ước tính tổn thất và cách kiểm chứng

Các phép tính sau dùng **giả định minh họa**, không phải số liệu thống kê của doanh nghiệp. Thời gian là khối lượng thao tác của nhân viên, chưa bao gồm hàng đợi; không quy đổi trực tiếp thành doanh thu bị mất.

| # bài toán | Giả định khối lượng và thời gian | Khối lượng thời gian tương ứng | Dữ liệu cần thu để kiểm chứng |
|---|---|---|---|
| 1 | 40 hóa đơn ngoại lệ/ngày × 6 phút/hóa đơn | 240 phút = 4 giờ công/ngày | Số hóa đơn ngoại lệ, thời gian đối soát và nguyên nhân sai lệch. |
| 2 | 60 ca hỗ trợ/ngày × 8 phút/ca | 480 phút = 8 giờ công/ngày | Log tiếp nhận, thời điểm xác minh và duyệt phương án; tách thời gian chờ. |
| 3 | 100 phản ánh/ngày × 5 phút/phản ánh | 500 phút ≈ 8,33 giờ công/ngày | Thời gian phân loại, tỷ lệ hỏi lại và tỷ lệ chuyển sai bộ phận. |
| 4 | 20 email/ngày × 12 phút/email | 240 phút = 4 giờ công/ngày | Thời gian đọc/nhập, số lần cập nhật và tỷ lệ phải sửa thông tin. |
| 5 | 30 ca khó xác định điểm đón/ngày × 3 phút trao đổi thêm/ca | 90 phút = 1,5 giờ/ngày trao đổi thêm của tài xế | Log gọi lại, thời gian tới điểm đón và lý do hủy; không cộng trùng thời gian khách chờ. |

Không cộng các hàng thành tổng tổn thất tập đoàn vì đây là các kịch bản giả định riêng biệt. Cần quan sát quy trình và đo baseline trước khi dùng để tính ROI.

### Chọn 3 bài toán để QUICK-ASSESS

- **Xanh SM — hỗ trợ pin yếu (#2):** Có ranh giới rõ để kiểm thử; cần phân biệt đề xuất AI và quyết định điều phối thực tế.
- **Vinhomes — phân loại phản ánh (#3):** Phù hợp thử khả năng hiểu mô tả tự do; đo được chất lượng phân loại và số lần hỏi lại.
- **VinFast — đối soát hóa đơn (#1):** Là trường hợp đối chứng để đánh giá khi nào rule-based đủ tốt, tránh dùng LLM không cần thiết.

Vinpearl (#4) cần xác minh cấu trúc email và quyền truy cập hệ thống đặt phòng. Điểm đón Xanh SM (#5) cần dữ liệu bản đồ/cổng vào đáng tin cậy; chỉ dùng LLM không giải quyết được sai lệch vị trí. Hai bài toán này được giữ lại để khảo sát sau.

## Phase 2 — QUICK-ASSESS (Cá nhân, 30 phút)

Chọn bài toán #2, #3 và #1 từ Phase 1, phân tích 10 phút/card. Thời gian hiện tại là giả định cần đo lại; metric là mục tiêu thử nghiệm, chưa phải kết quả đã đạt. Phản biện bên dưới là phân tích do AI hỗ trợ theo góc nhìn CFO và Trưởng phòng Vận hành, không phải ý kiến đã thu thập từ doanh nghiệp.

### QUICK PROBLEM CARD #1 — Xanh SM: bản nháp xử lý yêu cầu pin yếu

- **Bài toán (1 câu):** Điều phối viên mất nhiều thời gian xác minh tin nhắn pin yếu và soạn phương án hỗ trợ, khiến tài xế phải chờ.
- **Công ty thành viên:** [ ] VinFast · [x] Xanh SM · [ ] Vinhomes · [ ] Vinmec · [ ] Khác.
- **Actor:** Điều phối viên trực ca; người chịu ảnh hưởng là tài xế đang chờ hỗ trợ.
- **Workflow:** Nhận tin (1 phút) → kiểm tra pin/vị trí (2 phút) → tra cứu và soạn phương án (4 phút) → duyệt/gửi (1 phút).
- **Bottleneck:** Tra cứu và soạn nội dung, 4 phút/lượt; chuyển giao giữa chat, dữ liệu xe và người duyệt.
- **AI hỗ trợ ở bước nào?** Bước 3: LLM tạo đề xuất có cấu trúc và lý do ngắn từ thông tin đã xác minh; rule kiểm tra pin; con người xác minh và quyết định.
- **Metric mục tiêu:** Trung vị tổng thời gian 8 → ≤4 phút; p95 tạo nháp ≤15 giây; 0 gửi tự động; 100% ca pin <5% được chuyển đề xuất sạc di động trong bộ kiểm thử.
- **Quick Architecture:** [ ] No AI · [x] Rule · [x] LLM · [ ] Agent.
- **Operational Boundary:** Mọi đầu ra có nhãn `[DRAFT_ONLY]`. Pin <5% chỉ đề xuất sạc di động và chờ duyệt; prototype không chỉ đường đến trạm. Thiếu hoặc mâu thuẫn dữ liệu chuyển người. Không tự gửi, đặt chỗ, điều xe hoặc bịa ETA.

**Stress-test — 3 điểm yếu và hướng xử lý:**

1. **Logic:** Giảm thời gian soạn không bảo đảm tài xế được hỗ trợ nhanh hơn nếu không có phương tiện cứu hộ. Cần xác nhận dịch vụ hỗ trợ thực tế, đo riêng thời gian phản hồi và thời gian hỗ trợ đến nơi.
2. **Metric:** Baseline 8 phút và mục tiêu giảm 50% chưa có dữ liệu. Cần đo 100 ca baseline, tính cả thời gian duyệt/sửa và tách thời gian hàng đợi; không suy ra độ an toàn thực tế từ vài ca test.
3. **Chi phí / rule thay thế:** Rule đủ xử lý ngưỡng pin; template có thể đủ để soạn tin. So sánh rule + template với LLM trên cùng dữ liệu; chỉ giữ LLM nếu tiết kiệm thêm thời gian sau khi tính phí API, tích hợp và review.

### QUICK PROBLEM CARD #2 — Vinhomes: phân loại phản ánh cư dân

- **Bài toán (1 câu):** Nhân viên phải đọc và hỏi lại phản ánh cư dân thiếu cấu trúc trước khi phân loại và chuyển đúng bộ phận.
- **Công ty thành viên:** [ ] VinFast · [ ] Xanh SM · [x] Vinhomes · [ ] Vinmec · [ ] Khác.
- **Actor:** Nhân viên tiếp nhận ban quản lý.
- **Workflow:** Nhận phản ánh (1 phút) → đọc/xác định tòa (2 phút) → chọn bộ phận (1 phút) → nhập vé và chuyển (1 phút).
- **Bottleneck:** Đọc mô tả thiếu cấu trúc, 2 phút/lượt; dễ chuyển sai đội.
- **AI hỗ trợ ở bước nào?** Bước 2–3: LLM đề xuất nhãn và câu hỏi làm rõ, rule ánh xạ nhãn sang bộ phận; nhân viên xác nhận. Không đoán số tòa khi thiếu thông tin.
- **Metric mục tiêu:** Median thời gian thao tác 5 → ≤3 phút/vé, chưa tính chờ cư dân trả lời; macro-F1 ≥0,90 trên 200 vé giữ lại đã gán nhãn độc lập, không dùng chỉnh prompt; 100% vé thiếu tòa trong tập test được hỏi lại trước khi chuyển.
- **Quick Architecture:** [ ] No AI · [x] Rule · [x] LLM · [ ] Agent.
- **Boundary:** Không tự đóng vé, hứa thời hạn hoặc tiết lộ thông tin cư dân khác.

**Stress-test — 3 điểm yếu và hướng xử lý:**

1. **Logic:** Chuyển sai đội có thể do danh mục trách nhiệm chưa rõ. Cần thống nhất nhãn và chủ sở hữu từng loại vé trước khi dùng AI; vé mơ hồ chuyển người xử lý.
2. **Metric:** Macro-F1 cao chưa bảo đảm từng nhãn đều tốt. Cần báo cáo precision/recall từng loại, tỷ lệ chuyển sai và thời gian hỏi lại; kiểm tra riêng vé nhiều sự cố.
3. **Chi phí / rule thay thế:** Form bắt buộc chọn tòa và loại sự cố có thể giảm lỗi với chi phí thấp hơn. Lấy form + rule làm baseline; chỉ dùng LLM cho mô tả tự do nếu chứng minh được lợi ích bổ sung.

### QUICK PROBLEM CARD #3 — VinFast: đối chiếu hóa đơn sạc

- **Bài toán (1 câu):** Kế toán mất thời gian tra cứu và đối chiếu hóa đơn sạc ngoại lệ với dữ liệu phiên sạc để xác định chênh lệch.
- **Công ty thành viên:** [x] VinFast · [ ] Xanh SM · [ ] Vinhomes · [ ] Vinmec · [ ] Khác.
- **Actor:** Kế toán đối soát.
- **Workflow:** Nhận hóa đơn (1 phút) → nối mã phiên (1 phút) → so kWh/đơn giá (3 phút) → lập danh sách lệch chờ duyệt (1 phút).
- **Bottleneck:** So khớp dữ liệu, 3 phút/hóa đơn ngoại lệ.
- **AI hỗ trợ ở bước nào?** Chưa cần LLM. Ưu tiên code nối khóa và kiểm tra dung sai ở bước 2–3; OCR chỉ cân nhắc ở bước 1 nếu đầu vào là ảnh, sau đó người kiểm tra trường đọc được.
- **Metric mục tiêu:** Median thời gian xử lý 6 → ≤2 phút/ngoại lệ trên 100 hóa đơn ngoại lệ giữ lại có kết quả tham chiếu; 100% chênh lệch vượt dung sai đã thống nhất trong tập test được đưa vào danh sách duyệt; 0 thanh toán tự động.
- **Quick Architecture:** [ ] No AI · [x] Rule · [ ] LLM · [ ] Agent — OCR chưa thuộc phạm vi prototype.
- **Operational Boundary:** Không tự sửa hóa đơn, đoán mã phiên, thay số tiền hoặc duyệt thanh toán. Thiếu khóa hoặc không khớp phải đưa vào hàng chờ để kế toán xác minh.

**Stress-test — 3 điểm yếu và hướng xử lý:**

1. **Logic:** Thiếu mã phiên là vấn đề chất lượng dữ liệu, không thể giải quyết bằng việc để AI đoán mã. Cần trường mã bắt buộc và quy trình yêu cầu bổ sung dữ liệu nguồn.
2. **Metric:** Mục tiêu 2 phút có thể không đạt với ca thiếu mã. Không loại ca khó khỏi tập đo; báo cáo riêng ca đủ khóa, thiếu khóa và tổng thời gian xử lý có tính công tra cứu lại.
3. **Chi phí / rule thay thế:** Nối mã và so sánh tiền cần kết quả chính xác, truy vết được. Rule phù hợp hơn LLM; chỉ bổ sung OCR nếu lượng ảnh và chi phí nhập liệu chứng minh được lợi ích.

## Quyết định lựa chọn 

Quyết định chọn bài toán **“Card #1 — Xanh SM: Bản nháp xử lý yêu cầu pin yếu”** để thực hiện Deep-Dive trong phạm vi bài lab.

### Lý do lựa chọn và chưa chọn các thẻ khác

- **Card #1 (Xanh SM — Hỗ trợ pin yếu):** Bài toán hỗ trợ trực tiếp tài xế đang hoạt động, giúp giảm thời gian tra cứu và soạn phương án. AI chỉ tạo đề xuất để điều phối viên kiểm tra, phê duyệt trước khi gửi cho tài xế hoặc tổ chức hỗ trợ. Khi pin dưới 5%, hệ thống đề xuất hỗ trợ sạc di động; nếu thiếu thông tin, chuyển điều phối viên xử lý. Nhóm có thể đo hiệu quả qua thời gian xử lý và mức độ tuân thủ các quy tắc này.
- **Card #2 (Vinhomes — Phân loại phản ánh cư dân):** Có tiềm năng giảm thời gian tiếp nhận, nhưng cần thống nhất danh mục sự cố, bộ phận chịu trách nhiệm và dữ liệu gán nhãn để đánh giá việc chuyển đúng đội. Nhóm ưu tiên khảo sát form bắt buộc chọn tòa và rule-based router trước; chỉ cân nhắc LLM khi chứng minh được lợi ích với mô tả tự do. Vì vậy, chưa chọn bài toán này cho Deep-Dive ở vòng hiện tại.
- **Card #3 (VinFast — Đối chiếu hóa đơn sạc):** Phần công việc chính là nối mã phiên và so sánh điện năng, đơn giá, số tiền theo quy tắc xác định. Rule-based phù hợp hơn để bảo đảm tính chính xác và khả năng truy vết; LLM chưa có lợi ích bổ sung rõ ràng. Nhóm chưa chọn thẻ này cho Deep-Dive về LLM và giữ hướng đối soát bằng code thông thường.

Quyết định trên phục vụ lựa chọn phạm vi phân tích, chưa phải quyết định triển khai thực tế. Các giả định về thời gian, dữ liệu và năng lực hỗ trợ sẽ được đánh giá tiếp trong Phase 3 và Phase 5.
