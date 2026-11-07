# 🔍 Lab 02 — Phase 1 (SCAN) & Phase 2 (QUICK-ASSESS): AI Product Scoping (Vingroup)

> **Người thực hiện:** AI Product Engineer (Bài làm cá nhân) — **Tập đoàn Vingroup**  
> **Bài toán cá nhân lựa chọn:** **Vinmec Care Companion** — Trợ lý AI chăm sóc và theo dõi bệnh nhân sau xuất viện qua App/Zalo/SMS.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (4 Lenses)

Sử dụng **4 Lenses** (*Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác*) để quét qua hoạt động vận hành thực tế của các công ty thành viên Vingroup:

| # | Subsidiary | Lens | Mô tả ngắn bài toán (Operational Pain Point) |
|---|---|---|---|
| **1** | **🏥 Vinmec** | **Tốn thời gian & Pain từ người khác** | **Vinmec Care Companion (Theo dõi sau xuất viện):** Điều dưỡng phải gọi điện/nhắn tin Zalo thủ công cho hàng trăm bệnh nhân sau xuất viện để nhắc uống thuốc, nhắc lịch tái khám và hỏi thăm triệu chứng hằng ngày; việc đọc tin nhắn tự do để sàng lọc dấu hiệu biến chứng sớm mất 15–20 phút/bệnh nhân, dễ bỏ sót cảnh báo nguy cơ ngoài giờ hành chính. |
| **2** | **🏥 Vinmec** | **Tốn thời gian** | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Bác sĩ nội trú mất 20–30 phút/ca để tổng hợp kết quả xét nghiệm, chẩn đoán hình ảnh, diễn tiến điều trị từ HIS và chuyển thành hướng dẫn chăm sóc tại nhà dễ hiểu cho bệnh nhân. |
| **3** | **🚕 Xanh SM (GSM)** | **Tốn thời gian & Lặp lại** | **Xử lý sự cố sạc pin thực địa & Điều phối cứu hộ:** Điều phối viên mất 12–15 phút/sự cố để tra cứu vị trí GPS của xe báo yếu pin, tìm trụ sạc VinFast còn trống đúng chuẩn cổng sạc và soạn tin nhắn hướng dẫn tài xế hoặc điều xe cứu hộ pin di động. |
| **4** | **🏢 Vinhomes** | **AI có thể tốt hơn** | **Phân loại & Điều hướng phản ánh cư dân thông minh:** Tổng đài CSKH xử lý thủ công hàng nghìn phản ánh/ngày trên App Vinhomes Resident (điện nước, tiếng ồn, đăng ký thi công), phản hồi rập khuôn và mất trung bình 6–12 giờ để phân bổ đúng bộ phận kỹ thuật tòa nhà. |
| **5** | **🚗 VinFast** | **AI có thể tốt hơn** | **Chẩn đoán sơ bộ lỗi kỹ thuật từ mô tả ngôn ngữ tự nhiên:** Chủ xe mô tả hiện tượng bất thường bằng tiếng Việt đời thường (ví dụ: *"xe đi qua gờ giảm tốc kêu lục cục ở gầm trước"*), cố vấn dịch vụ mất nhiều thời gian tra cứu thủ công để quy đổi sang mã lỗi kỹ thuật và chuẩn bị phụ tùng trước khi xe vào xưởng. |
| **6** | **🎢 Vinpearl** | **Lặp lại** | **Bóc tách yêu cầu đặt phòng đoàn (Group Booking Email):** Nhân viên kinh doanh phải đọc thủ công hàng trăm email yêu cầu báo giá đoàn phức tạp từ đại lý du lịch (TA/OTA) để kiểm tra quỹ phòng trống và nhập liệu vào hệ thống PMS. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn **Top 3 bài toán** tiềm năng nhất từ danh sách SCAN (**#1 Vinmec Care Companion**, **#2 Vinmec Discharge Summary**, **#3 Xanh SM Sự cố sạc pin thực địa**) để đánh giá nhanh:

---

## 🏥 Card #1 — Vinmec Care Companion: Trợ lý AI chăm sóc & theo dõi sau xuất viện (Bài toán trọng tâm)

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                      │
│                                                                            │
│ Bài toán (1 câu): Bệnh nhân sau xuất viện quên uống thuốc, bỏ lỡ lịch tái  │
│ khám và không nhận diện sớm được dấu hiệu biến chứng tại nhà, trong khi     │
│ điều dưỡng quá tải với việc gọi điện/nhắn tin follow-up thủ công mỗi ngày.  │
│                                                                            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [x] Vinmec   [ ] Khác: ______________________________  │
│                                                                            │
│ Ai đang đau (Actor)?                                                       │
│ - Điều dưỡng chăm sóc hậu xuất viện (Follow-up Nurse): Quá tải gọi/nhắn    │
│   tin thủ công, tốn thời gian đọc phản hồi tự do để lọc ca bất thường.      │
│ - Bệnh nhân & Người nhà: Lo lắng khi có triệu chứng lạ tại nhà, dễ quên     │
│   liều thuốc hoặc nhầm lịch tái khám.                                      │
│ - Bác sĩ điều trị: Thiếu dữ liệu diễn tiến triệu chứng liên tục sau khi     │
│   bệnh nhân rời viện, dẫn đến phát hiện muộn biến chứng và tái nhập viện.   │
│                                                                            │
│ Workflow thủ công hiện tại (5 bước):                                       │
│   1. Trích xuất danh sách bệnh nhân xuất viện & y lệnh từ HIS ra Excel     │
│   ──> 2. Điều dưỡng nhắn Zalo/SMS nhắc uống thuốc & lịch tái khám          │
│   ──> 3. Gọi điện/nhắn tin hỏi thăm triệu chứng hằng ngày (Daily check-in) │
│   ──> 4. Đọc câu trả lời tự do, tự đánh giá mức nguy cơ & ghi chú vào HIS  │
│   ──> 5. Gọi báo bác sĩ trực khi phát hiện dấu hiệu bất thường/biến chứng  │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & Bước 4 (⏱ 14 phút/bệnh nhân/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                      │
│ - Bước 2 (Rule/Cron tự động gửi nhắc thuốc & lịch tái khám qua App/Zalo/SMS│
│ - Bước 3 & 4 (LLM thu thập phản hồi Daily Check-in, phân tích triệu chứng  │
│   ngôn ngữ tự nhiên, phân tầng nguy cơ Xanh/Vàng/Đỏ & tạo bản nháp cảnh    │
│   báo [DRAFT_ONLY] cho điều dưỡng/bác sĩ).                                 │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian follow-up thủ công của điều dưỡng từ 18 phút ──> < 3 phút │
│   /bệnh nhân/ngày (chỉ tập trung xử lý các ca nguy cơ Vàng/Đỏ).            │
│ - Rút ngắn thời gian phát hiện và cảnh báo sớm triệu chứng nguy cơ cao     │
│   từ 8-12 giờ ──> dưới 5 phút kể từ khi bệnh nhân phản hồi check-in.        │
│ - Tăng tỷ lệ tuân thủ uống thuốc & đúng hẹn tái khám từ 68% ──> trên 90%.  │
│ - Giảm 20-25% tỷ lệ tái nhập viện ngoài kế hoạch trong vòng 30 ngày.        │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (kết hợp Rule) [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏥 Card #2 — Vinmec: Trợ lý AI tóm tắt hồ sơ xuất viện (Discharge Summary Co-pilot)

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                      │
│                                                                            │
│ Bài toán (1 câu): Bác sĩ nội trú mất 25-30 phút cho mỗi ca xuất viện để    │
│ tổng hợp hồ sơ bệnh án điện tử (EMR) thành bản hướng dẫn xuất viện, gây    │
│ ùn tắc thủ tục ra viện buổi sáng.                                          │
│                                                                            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [x] Vinmec   [ ] Khác: ______________________________  │
│                                                                            │
│ Ai đang đau (Actor)? Bác sĩ điều trị / Bác sĩ nội trú & Bệnh nhân chờ xuất │
│ viện.                                                                      │
│                                                                            │
│ Workflow thủ công hiện tại (4 bước):                                       │
│   1. Mở nhiều tab trên HIS (xét nghiệm, CĐHA, phiếu phẫu thuật, đơn thuốc) │
│   ──> 2. Copy-paste & tổng hợp diễn tiến lâm sàng vào mẫu giấy ra viện     │
│   ──> 3. Viết lời dặn dò chế độ ăn uống, sinh hoạt và dấu hiệu cần khám lại│
│   ──> 4. Bác sĩ trưởng khoa ký duyệt và in trả bệnh nhân                   │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & Bước 3 (⏱ 22 phút/bệnh nhân)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Tổng hợp dữ liệu EMR và  │
│ soạn bản nháp tóm tắt hồ sơ xuất viện song ngữ / dễ hiểu cho bệnh nhân).   │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian soạn hồ sơ xuất viện từ 25 phút ──> dưới 5 phút/ca.       │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚕 Card #3 — Xanh SM: Trợ lý điều phối xử lý sự cố sạc pin thực địa

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                      │
│                                                                            │
│ Bài toán (1 câu): Tài xế Xanh SM báo cáo sự cố yếu pin / lỗi trụ sạc giữa  │
│ đường cần điều phối viên tìm trạm sạc trống phù hợp hoặc điều xe cứu hộ.   │
│                                                                            │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác: ______________________________  │
│                                                                            │
│ Ai đang đau (Actor)? Tài xế Xanh SM (chờ đợi) & Điều phối viên (quá tải).  │
│                                                                            │
│ Workflow thủ công hiện tại (5 bước):                                       │
│   1. Tài xế gọi tổng đài báo yếu pin / trụ sạc lỗi                         │
│   ──> 2. Điều phối viên tra cứu tọa độ GPS của xe trên bản đồ              │
│   ──> 3. Mở dashboard trạm sạc VinFast tìm trụ trống phù hợp dòng xe       │
│   ──> 4. Soạn tin nhắn chỉ dẫn lộ trình gửi qua App Tài xế                 │
│   ──> 5. Gọi đội xe sạc pin lưu động nếu pin dưới ngưỡng an toàn (< 5%)    │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & Bước 4 (⏱ 10 phút/lượt)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4 (Tự động khớp tọa độ với  │
│ API trạm sạc trống và soạn bản nháp [DRAFT_ONLY] hoặc lệnh cứu hộ).        │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt.              │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                │
└────────────────────────────────────────────────────────────────────────────┘
```

---

# ⚖️ Phản biện (Stress-Test) & Quyết định lựa chọn bài toán Deep-Dive (Cá nhân)

### 1. Kết quả Stress-Test với góc nhìn CFO & Trưởng khối Vận hành Y tế (Vinmec):
Khi đưa **Card #1 (Vinmec Care Companion)** qua bộ câu hỏi phản biện khắt khe (*"Tại sao không dùng Rule-based / trắc nghiệm nút bấm thông thường mà cần đến LLM?"*), tôi đã làm rõ 3 điểm cốt lõi:
1. **Tại sao Rule-based đơn thuần thất bại ở bước Daily Check-in triệu chứng?**
   - **Rule-based / Cron-job** giải quyết rất tốt việc nhắc giờ uống thuốc và nhắc lịch tái khám cố định (và tôi **giữ nguyên Rule-based** cho phần này để tiết kiệm chi phí, độ chính xác 100%).
   - Tuy nhiên, khi bệnh nhân trả lời Daily Check-in qua Zalo/SMS hoặc App, bệnh nhân Việt Nam (đặc biệt là người cao tuổi hoặc sau phẫu thuật) thường mô tả bằng **ngôn ngữ tự nhiên đa dạng, giàu phương ngữ và ngữ cảnh** (ví dụ: *"Hôm nay bác uống thuốc xong thấy hơi xây xẩm mặt mày, vết mổ ở bụng thì không chảy dịch nữa nhưng xung quanh hơi ấm ấm và tức nhẹ khi ho"*). Một form nút bấm cứng nhắc (Có/Không) vừa có tỷ lệ hoàn thành thấp, vừa không bắt được các sắc thái kết hợp triệu chứng (như tác dụng phụ của thuốc hạ áp kèm dấu hiệu nhiễm trùng vết mổ sớm).
2. **Kiểm soát rủi ro lâm sàng (Medical Safety Boundary):**
   - AI **tuyệt đối không đóng vai bác sĩ chẩn đoán hay tự ý đổi liều thuốc**. Vai trò của LLM được khóa chặt ở tác vụ **Clinical Symptom Extraction & Risk Triage (Trích xuất triệu chứng, đối chiếu Red Flags theo phác đồ xuất viện của từng bệnh lý, xếp mức nguy cơ Xanh / Vàng / Đỏ)** và tạo bản nháp cảnh báo `[DRAFT_ONLY]` để điều dưỡng/bác sĩ phê duyệt (Human-in-the-loop).
3. **Lợi ích kinh tế (ROI) rõ ràng:**
   - Thay vì 1 điều dưỡng chỉ có thể gọi điện thủ công cho 25–30 bệnh nhân/ngày (mất 15–18 phút/người, phần lớn là các ca bình thường), **Vinmec Care Companion** tự động hóa việc thu thập & sàng lọc sơ bộ cho hàng nghìn bệnh nhân, giúp điều dưỡng chỉ cần can thiệp sâu vào **10–15% nhóm bệnh nhân có dấu hiệu Vàng/Đỏ**, giảm tải > 80% thời gian follow-up thủ công và ngăn ngừa biến chứng nặng phải tái nhập viện cấp cứu.

### 2. Quyết định lựa chọn của cá nhân tôi:
Tôi quyết định chọn **Card #1 — Vinmec Care Companion (Trợ lý AI chăm sóc sau xuất viện)** để thực hiện **Phase 3 (Deep-Dive)**, **Phase 4 (Prompt Prototype)** và **Phase 5 (Evaluate)** tại file `02-deep-dive-report.md`.
* **Lý do chưa chọn Card #2 (Vinmec Discharge Summary):** Tuy tiết kiệm thời gian cho bác sĩ nội trú nhưng tác động chỉ dừng ở khâu hành chính lúc ra viện, không giải quyết được rủi ro biến chứng và tái nhập viện trong 30 ngày sau xuất viện.
* **Lý do chưa chọn Card #3 (Xanh SM Sự cố sạc pin):** Bài toán hậu xuất viện tại Vinmec mang lại giá trị nhân văn và tác động trực tiếp hơn đến an toàn tính mạng người bệnh cũng như giảm tải áp lực theo dõi liên tục 24/7 cho đội ngũ y tế.

