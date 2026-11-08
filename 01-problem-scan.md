# 01 — Problem Scan & Quick Assess (Cá nhân)

> **Lab 02 — AI Product Scoping (Vin Smart Future)**
> **Mảng kinh doanh lựa chọn:** VinFast — Hệ thống xe điện thông minh (EV).
> **Bài toán trọng tâm:** Dự đoán bảo trì pin (Predictive Battery Maintenance).

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Sử dụng **4 Lenses** để quét qua hoạt động vận hành của VinFast.
Ưu tiên các quy trình thủ công, tốn thời gian và gây rò rỉ hiệu suất trong mảng dịch vụ & xe điện.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | Tốn thời gian | Kỹ thuật viên xưởng dịch vụ phải đọc thủ công hàng nghìn dòng dữ liệu telemetry (lịch sử sạc, nhiệt độ pin, số chu kỳ sạc) để phán đoán tình trạng sức khỏe pin (State of Health - SoH) của từng xe — mất 20-30 phút/xe. |
| 2 | **VinFast** | Lặp lại | Hệ thống ghi nhận hàng trăm cảnh báo lỗi (DTC - Diagnostic Trouble Code) từ các xe gửi về mỗi ngày, nhân viên phải phân loại thủ công đâu là lỗi thật cần xử lý, đâu là cảnh báo nhiễu. |
| 3 | **VinFast** | AI có thể tốt hơn | Trợ lý ảo trong xe (in-car assistant) hiện chỉ trả lời theo kịch bản cứng, chưa giải thích được cho tài xế ý nghĩa cảnh báo pin và cách xử lý phù hợp theo ngữ cảnh thực tế (quãng đường còn lại, trạm sạc gần nhất). |
| 4 | **VinFast** | Pain từ người khác | Chủ xe phàn nàn pin bị chai/xuống cấp bất ngờ mà không có cảnh báo trước, dẫn đến sự cố hết pin giữa đường và tranh chấp bảo hành với hãng. |
| 5 | **VinFast** | Tốn thời gian | Soạn báo cáo tình trạng pin (SoH report) cho khách trước khi hết hạn bảo hành phải làm thủ công, mất nhiều giờ cho mỗi lô xe, dễ sai sót số liệu. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn **top 3** từ danh sách SCAN: **#1 (Dự đoán bảo trì pin), #2 (Phân loại cảnh báo DTC), #5 (Báo cáo SoH trước hết bảo hành).**

## ⭐ Thẻ bài toán trọng tâm: Card #1 — Dự đoán bảo trì pin (Predictive Battery Maintenance)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Dự đoán sớm thời điểm và mức độ suy giảm  │
│ pin của xe VinFast từ dữ liệu telemetry để chủ động đề xuất │
│ bảo trì, thay vì để khách phát hiện khi pin đã hỏng nặng.   │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)? Kỹ thuật viên xưởng dịch vụ (đọc dữ    │
│ liệu thủ công) và Trung tâm CSKH (xử lý khiếu nại pin).     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Xe gửi dữ liệu telemetry (lịch sử sạc, nhiệt độ, DTC)  │
│   ──> 2. Kỹ thuật viên mở từng bảng log, kiểm tra thủ công  │
│   ──> 3. Tra cứu lịch sử bảo trì + chính sách bảo hành      │
│   ──> 4. Phán đoán SoH bằng kinh nghiệm, ghi chú rời rạc    │
│   ──> 5. Viết khuyến nghị bảo trì và liên hệ khách hàng     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4 (⏱ 25 phút/xe,    │
│ phụ thuộc kinh nghiệm kỹ thuật viên, dễ bỏ sót dấu hiệu)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4 (tự động     │
│ trích xuất dấu hiệu suy giảm pin -> tạo draft khuyến nghị)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm thời gian đánh giá từ 25 phút ──> dưới 5 phút/xe.   │
│ 2. Phát hiện đúng ≥ 90% xe có dấu hiệu suy giảm pin trước   │
│    khi khách khiếu nại (Recall).                            │
│                                                             │
│ Quick Architecture: [x] LLM Feature (trích xuất + soạn draft │
│ khuyến nghị bảo trì, có người duyệt)                        │
└─────────────────────────────────────────────────────────────┘
```

## Card #2 — Phân loại cảnh báo lỗi (DTC) tự động

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và ưu tiên hàng trăm    │
│ cảnh báo lỗi (DTC) từ xe gửi về mỗi ngày thành "cần xử lý   │
│ ngay" / "theo dõi" / "nhiễu".                               │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)? Trung tâm giám sát kỹ thuật (Technical │
│ Support Center) tiếp nhận cảnh báo từ đội xe.               │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đội xe gửi danh sách mã lỗi (DTC)                      │
│   ──> 2. Nhân viên tra cứu từng mã lỗi theo tài liệu        │
│   ──> 3. Đối chiếu với mô hình xe + lịch sử sửa chữa        │
│   ──> 4. Gắn nhãn ưu tiên và chuyển tới xưởng               │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 30-45 phút/    │
│ lô cảnh báo, dễ bỏ sót lỗi pin quan trọng)                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (phân loại   │
│ + giải thích mã lỗi + gợi ý mức ưu tiên)                    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Phân loại đúng ≥ 95%, giảm thời gian xử lý lô cảnh báo từ   │
│ 45 phút ──> dưới 5 phút.                                    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (kết hợp Rule lọc trước)│
└─────────────────────────────────────────────────────────────┘
```

## Card #3 — Báo cáo tình trạng pin (SoH) trước hết bảo hành

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tự động soạn báo cáo tình trạng pin        │
│ (State of Health) cho từng xe trước khi hết hạn bảo hành.   │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)? Bộ phận Bảo hành & Kỹ thuật viên       │
│ (phải tổng hợp số liệu thủ công cho hàng loạt xe).          │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Lọc danh sách xe sắp hết bảo hành                      │
│   ──> 2. Xuất dữ liệu sạc/telemetry từng xe                 │
│   ──> 3. Tính toán & viết nhận xét tình trạng pin           │
│   ──> 4. Gửi báo cáo cho khách, lưu hồ sơ                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 15 phút/xe,    │
│ sai sót số liệu khi làm thủ công)                           │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 (tổng hợp số   │
│ liệu -> soạn draft báo cáo ngôn ngữ dễ hiểu cho khách)      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn báo cáo từ 15 phút ──> dưới 3 phút/xe,  │
│ độ chính xác số liệu 100% (không sai lệch dữ liệu gốc).     │
│                                                             │
│ Quick Architecture: [x] LLM Feature (draft báo cáo có người │
│ kiểm duyệt trước khi gửi khách)                             │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn

Bài toán được chọn để thực hiện **Deep-Dive** (chuyển sang `02-deep-dive-report.md`):

> **Card #1 — Dự đoán bảo trì pin (Predictive Battery Maintenance).**

**Lý do lựa chọn:**
* **Business impact lớn và đo lường được:** Suy giảm pin là nguyên nhân hàng đầu gây khiếu nại bảo hành và sự cố hết pin giữa đường, ảnh hưởng trực tiếp đến chi phí bảo hành và uy tín thương hiệu.
* **Metric rõ ràng:** SoH, Recall phát hiện sớm, thời gian đánh giá/xe đều là các con số định lượng được.
* **AI Fit phù hợp:** Dữ liệu telemetry là dạng bán cấu trúc → LLM trích xuất dấu hiệu + soạn khuyến nghị bảo trì (draft) là hợp lý, không cần đến multi-agent.

**Lý do loại bỏ các thẻ khác:**
* **Card #2 (Phân loại DTC):** Đây chủ yếu là bài toán phân loại có cấu trúc, **Rule-based filter + classifier** truyền thống có thể đã đủ tốt, chưa cần đến LLM để tạo khác biệt lớn.
* **Card #3 (Báo cáo SoH):** Có giá trị nhưng phạm vi hẹp (back-office định kỳ), ít ảnh hưởng tới vận hành thời gian thực so với việc phát hiện sớm suy giảm pin của Card #1.

---

# ⚠️ Ranh giới vận hành (Operational Boundary) — Định hướng ban đầu

Định hướng ranh giới cho bài toán Card #1 (sẽ được hoàn thiện ở Phase 3 & Phase 4):
1. **Human-in-the-loop bắt buộc:** AI chỉ được tạo **bản nháp (draft)** khuyến nghị bảo trì, tuyệt đối không tự động gửi cho khách hàng hoặc tự động ra lệnh thay thế pin.
2. **Không chẩn đoán thay kỹ thuật viên:** AI không được kết luận "pin hỏng, phải thay" — chỉ nêu dấu hiệu và đề xuất kiểm tra.
3. **Ngưỡng an toàn pin:** Khi mức pin ở ngưỡng nguy hiểm (< 5%), AI phải ưu tiên đề xuất điều xe sạc pin di động (mobile charger) thay vì hướng dẫn cố di chuyển tới trạm sạc xa.
