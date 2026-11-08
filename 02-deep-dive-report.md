# 02 — Deep-Dive Report (Nhóm)

> **Lab 02 — AI Product Scoping (Vin Smart Future)**
> **Mảng kinh doanh lựa chọn:** VinFast — Hệ thống xe điện thông minh (EV).
> **Bài toán Deep-Dive:** Dự đoán bảo trì pin (Predictive Battery Maintenance).
> **Nguồn gốc:** Chuyển tiếp từ `01-problem-scan.md` — **Card #1**.

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi là lập trình viên AI tại **Vin Smart Future**, được giao phối hợp với Khối Dịch vụ & Kỹ thuật của **VinFast**. Qua quan sát tại một xưởng dịch vụ, tôi thấy các **kỹ thuật viên (KTV)** đang phải đọc thủ công khối lượng lớn dữ liệu telemetry của pin (lịch sử sạc, nhiệt độ, số chu kỳ, mã lỗi) để phán đoán tình trạng sức khỏe pin (**SoH — State of Health**) cho từng xe. Việc này tốn thời gian, phụ thuộc kinh nghiệm và dễ bỏ sót dấu hiệu suy giảm sớm — dẫn tới sự cố hết pin giữa đường và tranh chấp bảo hành. Đây chính là bài toán tôi mang vào Deep-Dive.

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)

## 3.1. Current-State Workflow Mapping

Quy trình đánh giá tình trạng pin cho một xe tại xưởng dịch vụ VinFast hiện tại:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Nhận danh    │     │ Xuất dữ liệu │     │ Đọc & phân   │
│ sách xe cần  │ ──→ │ telemetry    │ ──→ │ tích log pin │
│ đánh giá pin │     │ của từng xe  │     │ thủ công     │
│              │     │              │     │              │
│ Ai: Điều phối│     │ Ai: Hệ thống │     │ Ai: KTV      │
│ ⏱ 2 phút     │     │ ⏱ 1 phút 🔄  │     │ ⏱ 10 phút 🔴 │
│ In: Yêu cầu  │     │ In: Mã xe    │     │ In: Raw logs │
│ Out: Mã xe   │     │ Out: Raw log │     │ Out: Ghi chú │
└──────────────┘     └──────────────┘     └──────────────┘
                                                 │
                                                 ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 6       │     │ Bước 5       │     │ Bước 4       │
│ Soạn khuyến  │     │ Ước lượng    │     │ Tra cứu lịch │
│ nghị bảo trì │ ←── │ SoH bằng     │ ←── │ sử bảo trì + │
│ + liên hệ KH │     │ kinh nghiệm  │     │ chính sách BH│
│              │     │              │     │              │
│ Ai: KTV      │     │ Ai: KTV      │     │ Ai: KTV      │
│ ⏱ 4 phút     │     │ ⏱ 6 phút 🔴  │     │ ⏱ 2 phút     │
│ In: Nhận xét │     │ In: Ghi chú  │     │ In: Lịch sử  │
│ Out: Tin nhắn│     │ Out: SoH draft│    │ Out: Hồ sơ   │
└──────────────┘     └──────────────┘     └──────────────┘

🔴 = Bottleneck   🔄 = Handoff (người ⇄ hệ thống)
⏱ Tổng thời gian xử lý thủ công: 25 phút/xe.
```

* **🔴 Bottleneck chính:** **Bước 3 (10 phút)** và **Bước 5 (6 phút)** — chiếm ~64% tổng thời gian. Đây là khâu đọc log thô và phán đoán SoH bằng kinh nghiệm, dễ sai sót và không nhất quán giữa các KTV.
* **🔄 Handoff:** **Bước 2** — dữ liệu telemetry chuyển từ hệ thống sang KTV thủ công (copy/paste, dễ mất ngữ cảnh).

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Kỹ thuật viên (KTV) xưởng dịch vụ VinFast; phối hợp với Trung tâm CSKH khi có khiếu nại pin. |
| **2. Current Workflow** | Khi xe đến kỳ kiểm tra hoặc có khiếu nại về pin, KTV xuất dữ liệu telemetry (lịch sử sạc, nhiệt độ, số chu kỳ, mã lỗi), đọc và phân tích log thủ công, tra cứu lịch sử bảo trì + chính sách bảo hành, ước lượng SoH bằng kinh nghiệm, rồi soạn khuyến nghị và liên hệ khách. **6 bước, hoàn toàn thủ công, ~25 phút/xe.** |
| **3. Bottleneck** | **Bước 3 & 5 (~16 phút):** đọc/parse khối log telemetry cồng kềnh và phán đoán SoH *không theo một chuẩn thống nhất*, phụ thuộc kinh nghiệm từng KTV → dễ bỏ sót dấu hiệu suy giảm sớm. |
| **4. Business Impact** | **[GIẢ ĐỊNH — cần xác thực bằng dữ liệu nội bộ]** Nếu mỗi trung tâm xử lý ~40 xe cần đánh giá pin/tuần → ~16,7 giờ/tuần/trung tâm chỉ riêng việc đọc log thủ công. Bỏ sót dấu hiệu suy giảm dẫn tới sự cố hết pin giữa đường, tăng chi phí bảo hành và rủi ro tranh chấp với khách. |
| **5. Success Metric** | 1. Giảm thời gian đánh giá từ **25 phút → dưới 5 phút/xe** (Efficiency).<br>2. **Recall ≥ 90%**: phát hiện đúng xe có dấu hiệu suy giảm pin *trước khi* khách khiếu nại (Quality).<br>3. **Tỉ lệ draft được KTV chấp nhận (không sửa) ≥ 80%** (Usability). |
| **6. Operational Boundary** | **Được phép:** đọc telemetry, trích xuất dấu hiệu suy giảm, tạo **bản nháp (draft)** khuyến nghị bảo trì.<br>**TUYỆT ĐỐI KHÔNG:** tự động gửi cho khách hàng; tự ra lệnh thay pin; kết luận thay KTV rằng "pin hỏng, phải thay".<br>**Ngưỡng an toàn:** khi pin < **5%** → bắt buộc trả `{"action": "dispatch_mobile_charger", ...}` thay vì hướng dẫn di chuyển tới trạm xa.<br>**Bắt buộc HITL:** mọi kết quả AI đều phải được KTV duyệt trước khi gửi khách. |

---

## 3.3. Future-State Flow & AI Fit

### AI-Fit Matrix — so sánh 3 mức

| Mức | Cách tiếp cận | Đánh giá cho bài toán này |
|---|---|---|
| **Rule / State-Machine** | Ngưỡng cứng: SoH < 80% → gắn cờ; nhiệt độ > X → cảnh báo | Nhanh, rẻ, nhưng **bỏ sót pattern phức tạp** (suy giảm thể hiện qua *tổ hợp* chu kỳ + nhiệt độ + hành vi sạc) và không giải thích được bằng ngôn ngữ tự nhiên. |
| **✅ LLM Feature (chọn)** | LLM đọc telemetry bán cấu trúc → **trích xuất dấu hiệu** + **soạn draft khuyến nghị** dễ hiểu; kết hợp lớp ngưỡng rule để chốt an toàn | Đúng thế mạnh: xử lý log lộn xộn + diễn giải ngôn ngữ; rủi ro thấp nhờ HITL. **Không cần huấn luyện model** → không phụ thuộc dữ liệu gán nhãn lớn. |
| **Agentic Loop** | Agent tự truy vấn, tự ra quyết định, tự gửi | **Quá đà**: quy trình có cấu trúc cố định, và rủi ro an toàn (chẩn đoán sai pin) quá cao để AI tự trị. |

> **Kết luận AI Fit:** chọn **LLM Feature** (kết hợp lớp rule-based cho ngưỡng an toàn). Lý do: bài toán nặng về *ngôn ngữ + trích xuất từ log lộn xộn*, không phải bài toán cần suy luận đa bước tự trị.

### Future-State Flow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Nhận danh    │     │ 🔵 Auto-pull │     │ 🔵 AI phân   │
│ sách xe      │ ──→ │ telemetry +  │ ──→ │ tích log,    │
│ (như cũ)     │     │ 🔵 AI trích  │     │ phát hiện    │
│              │     │ xuất dấu hiệu│     │ rủi ro SoH   │
└──────────────┘     └──────────────┘     └──────────────┘
                                                 │
                                                 ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ ↩️ Fallback  │     │ 🟢 KTV duyệt │     │ 🔵 AI draft  │
│ AI lỗi/không │     │ (HITL) sửa & │     │ khuyến nghị  │
│ tự tin → KTV │ ←── │ gửi khách    │ ←── │ bảo trì      │
│ tự làm thủ   │     │              │     │              │
│ công như cũ  │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘

🔵 = AI Step   🟢 = Human Step (HITL)   ↩️ = Fallback
```

* **🔵 AI Step (Bước 2–3, 4):** tự động lấy telemetry, trích xuất dấu hiệu suy giảm, soạn draft khuyến nghị.
* **🟢 Human Step (HITL):** KTV **duyệt/sửa** draft trước khi gửi khách — AI không bao giờ tự gửi.
* **↩️ Fallback:** nếu AI lỗi, không tự tin, hoặc KTV từ chối kết quả → quay về quy trình thủ công hiện tại (không chặn công việc).

---

# 💻 Phase 4 — Prompt Prototype (tham chiếu)

Nhóm đã hiện thực ranh giới an toàn của bài toán trong [prompt_prototype.py](prompt_prototype.py) và kiểm thử bằng **Gemini** thông qua các **adversarial test**:

* **Ranh giới 1:** mọi output phải bắt đầu bằng `[DRAFT_ONLY]` (chống bị dụ "gửi thẳng luôn").
* **Ranh giới 2:** pin < 5% → cấm gợi ý trạm > 5km, **bắt buộc** trả `{"action": "dispatch_mobile_charger", ...}`.
* **Ranh giới 3:** không tự chẩn đoán "pin hỏng" / không tự ra lệnh thay pin.

> Chi tiết kết quả kiểm thử được ghi trong `03-ai-log.md`.

---

# 🏁 Phase 5 — EVALUATE (Nhóm)

## AI Readiness Checklist

| # | Câu hỏi | Trả lời | Ghi chú |
|---|---|---|---|
| 1 | Có sẵn dữ liệu mẫu/logs sạch để test? | ⚠️ **Một phần** | Telemetry có sẵn, nhưng cần làm sạch + lấy mẫu log để xác lập **baseline** trước khi mở rộng. Vì chọn **LLM Feature (không huấn luyện)** nên chưa cần tập gán nhãn lớn. |
| 2 | Rủi ro khi AI sai có trong tầm kiểm soát? | ✅ **Có** | HITL bắt buộc + Fallback về quy trình thủ công + `[DRAFT_ONLY]` + ngưỡng an toàn pin. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình cũ? | ✅ **Cơ bản có** | KTV muốn giảm việc đọc log thủ công; cần đào tạo ngắn về cách duyệt draft. |

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

> ✅ **GO (Bắt đầu xây dựng Prototype với scope hẹp)**

**Justification (dựa trên bằng chứng kỹ thuật & chi phí):**

1. **Bài toán cụ thể, metric định lượng được:** thời gian/xe (25 → <5 phút), Recall phát hiện sớm (≥90%) — đo được từ log nội bộ.
2. **Giải pháp đơn giản, hiệu quả (problem-first):** **LLM Feature** không cần huấn luyện model riêng → chi phí thấp, triển khai nhanh, trái ngược với các đề xuất "over-engineering" (multi-agent, fine-tune) mà AI từng gợi ý.
3. **Rủi ro được kiểm soát chặt:** ranh giới vận hành đã được **viết cứng** và **kiểm thử bằng adversarial test**, kết hợp HITL + Fallback → AI sai không gây hậu quả trực tiếp cho khách.
4. **Điều kiện đi kèm (scope hẹp):** chỉ triển khai **pilot tại 1 trung tâm dịch vụ**, ở chế độ **draft-only**, và **xác lập baseline trên mẫu log sạch** trước khi mở rộng.
