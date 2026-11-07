# Problem Statement: Tìm kiếm người thất lạc bằng AI Re-ID (Person Re-identification)

## 1. Bối cảnh & Vấn đề thực địa
**Bối cảnh:** Vinpearl & VinWonders sở hữu các khu quần thể du lịch, vui chơi giải trí có diện tích rất rộng (hàng trăm hecta) với hàng chục ngàn lượt khách mỗi ngày. 

**Vấn đề:** 
- Diện tích quá rộng khiến nhân viên bảo vệ không thể bao quát hết toàn bộ khu vực.
- Tình trạng trẻ em đi lạc, khách đi lạc hoặc thất lạc người thân diễn ra thường xuyên, đặc biệt vào mùa cao điểm.
- Các hành vi vi phạm (trộm cắp, chen hàng, xâm nhập khu vực cấm) khó phát hiện kịp thời bằng mắt thường.
- **Quy trình hiện tại:** Khi có báo mất tích, nhân viên an ninh phải tua lại camera thủ công bằng mắt thường. Quá trình này rất tốn thời gian (30-60 phút), làm mất đi "thời gian vàng" để tìm kiếm trẻ.

**Giải pháp AI đề xuất:**
Ứng dụng công nghệ **Person Re-identification (Re-ID)**. Khi nhận được ảnh của người thất lạc, AI sẽ tự động quét lại toàn bộ dữ liệu camera trong 1-2 giờ qua, trích xuất đặc điểm ngoại hình (quần áo, màu tóc, dáng đi) và đưa ra cảnh báo vị trí cuối cùng người đó xuất hiện.

---

## 2. Phân tích 6 trường (6-Field Framework)

### 2.1. Actor / Operator (Các bên liên quan & Người vận hành)
*   **Actor (Người gặp vấn đề):**
    *   **Khách hàng (Phụ huynh):** Người đang hoảng loạn, cần tìm lại con/người thân ngay lập tức.
    *   **Trẻ em/Người đi lạc:** Đối tượng cần được tìm thấy.
*   **Operator (Người trực tiếp vận hành hệ thống):**
    *   **Nhân viên trực Camera (Security Control Room):** Người nhận lệnh, thao tác tải ảnh lên hệ thống, chạy tìm kiếm và đọc kết quả.
    *   **Đội tuần tra/Bảo vệ hiện trường (Ground Patrol):** Người nhận cảnh báo vị trí trên bộ đàm/điện thoại và tiếp cận đứa trẻ.
    *   **Lễ tân/CSKH:** Người tiếp nhận thông tin ban đầu từ phụ huynh.

### 2.2. Workflow (Luồng công việc)
1.  **Tiếp nhận:** Phụ huynh báo mất tích tại quầy CSKH. Nhân viên ghi nhận thông tin (mô tả ngoại hình, trang phục) và xin 1 bức ảnh rõ nhất của trẻ (nếu có).
2.  **Đưa vào hệ thống:** Nhân viên Control Room tải bức ảnh lên giao diện Re-ID. Hệ thống tự động trích xuất đặc trưng (vector nhúng - embedding) của trẻ.
3.  **Truy vết tự động:** Hệ thống tự động quét luồng video lưu trữ (NVR) của tất cả các camera trong khu vực trong vòng 1-2 giờ qua. AI so khớp vector của trẻ với tất cả người xuất hiện trong video.
4.  **Trả kết quả:** Hệ thống hiển thị một "Timeline" (dòng thời gian) các sự kiện: Trẻ xuất hiện ở camera A lúc 10:05, đi về hướng camera B lúc 10:07, xuất hiện lần cuối ở khu vực C lúc 10:15.
5.  **Điều phối:** Control Room gửi vị trí cuối cùng và hướng di chuyển cho đội bảo vệ gần nhất qua bộ đàm. Bảo vệ tiếp cận và đưa trẻ về.

### 2.3. Bottleneck (Điểm nghẽn / Thách thức)
*   **Điểm nghẽn Vận hành (Con người):**
    *   Tua camera thủ công mất 30-60 phút.
    *   Phụ huynh hoảng loạn không nhớ chính xác mô tả trang phục.
    *   Bảo vệ hiện trường không biết chính xác trẻ đang ở đâu, chỉ có thể tỏa ra các hướng để tìm bằng mắt.
*   **Điểm nghẽn Kỹ thuật (AI):**
    *   **Chất lượng ảnh đầu vào kém:** Ảnh selfie cận mặt vs Camera an ninh chụp toàn thân từ xa, góc xiên, ngược sáng.
    *   **Sự thay đổi ngoại hình:** Trẻ có thể đã cởi áo khoác, đội thêm mũ, hoặc bị bẩn quần áo.
    *   **Mật độ đám đông (Occlusion):** Trẻ bị che khuất tầm nhìn của camera (bị người lớn che mất).
    *   **False Positives (Nhận diện nhầm):** Nhiều trẻ mặc trang phục giống nhau khiến AI trả về hàng trăm kết quả, làm nhân viên rối trí.

### 2.4. Businesses Impact (Tác động đến Kinh doanh)
*   **Tích cực (ROI):**
    *   **Tăng NPS & Uy tín thương hiệu:** Xử lý thất lạc nhanh chóng tạo ra sự an tâm tuyệt đối, điểm cộng cực lớn cho khu nghỉ dưỡng gia đình.
    *   **Giảm chi phí vận hành:** Không cần huy động 20 bảo vệ tỏa ra tìm kiếm trong 1 giờ (tốn nhân lực, ảnh hưởng an ninh khu vực khác).
    *   **Giảm rủi ro pháp lý & truyền thông:** Tìm thấy nhanh (dưới 10-15 phút) biến sự cố thành câu chuyện khoe dịch vụ.
*   **Tiêu cực (Nếu hệ thống lỗi):** Cảnh báo sai (False Alarm) quá nhiều khiến bảo vệ mệt mỏi (Alert Fatigue), hoặc tìm sai người khiến mất thời gian vàng.

### 2.5. Success Metric (Chỉ số đo lường thành công)
*   **Time-to-Find (TTF):** Thời gian từ lúc nhận ảnh đến lúc đưa ra cảnh báo vị trí cuối cùng (Mục tiêu: **< 3 phút** quét toàn bộ 2 giờ video).
*   **Top-K Accuracy:** Tỷ lệ người thất lạc thực sự nằm trong Top 3 hoặc Top 5 kết quả AI gợi ý (Mục tiêu: **> 90%** trong Top 5).
*   **False Positive Rate (FPR):** Tỷ lệ cảnh báo nhầm (Hệ thống báo thấy ở camera A nhưng thực tế không phải).
*   **Search Recall:** Tỷ lệ % các lần hệ thống tìm ra được dấu vết của người thất lạc trong camera (Mục tiêu: **> 85%**).

### 2.6. Operation Boundary (Ranh giới Vận hành & Phạm vi)
*   **Ranh giới Kỹ thuật:**
    *   Chỉ hoạt động trong vùng phủ của Camera (Blind spots - điểm mù như nhà vệ sinh, khu khuất cây cối sẽ không quét được).
    *   Yêu cầu camera đạt chuẩn tối thiểu (độ phân giải 1080p, khung hình 15fps, không bị mờ).
    *   Chỉ tìm kiếm trên dữ liệu lưu trữ (tối đa 24h-48h gần nhất tùy dung lượng ổ cứng NVR).
*   **Ranh giới Đạo đức & Pháp lý (Cực kỳ quan trọng):**
    *   Chỉ được phép chạy Re-ID khi có **yêu cầu chính thức từ phụ huynh/người giám hộ** và có sự phê duyệt của Trưởng bộ phận An ninh (tránh lạm dụng rình rập).
    *   Dữ liệu hình ảnh/vector trích xuất phải được mã hóa và **tự động xóa (auto-delete)** sau 24 giờ hoặc ngay khi tìm thấy người. Không lưu trữ lâu dài để huấn luyện model (tránh vi phạm quyền riêng tư).
*   **Ranh giới Vận hành:**
    *   AI chỉ đưa ra **Gợi ý/Cảnh báo (Decision Support)**, quyết định tiếp cận và xác minh cuối cùng vẫn phải do con người (Bảo vệ) thực hiện.

---

## 3. Đề xuất triển khai PoC (Proof of Concept)
*   **Không train model từ đầu:** Sử dụng các Open-source Model như **Torchreid** hoặc giải pháp thương mại (BriefCam, SenseTime) để PoC.
*   **Giao diện UI đơn giản:** Thiết kế UI cho nhân viên an ninh theo luồng: Kéo thả ảnh -> Bấm "Tìm" -> Hiện bản đồ có các điểm sáng (vị trí người xuất hiện).