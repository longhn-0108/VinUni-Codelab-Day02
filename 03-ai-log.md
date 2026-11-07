# Nhật ký sử dụng AI

Trong bài này, mình dùng AI để hỗ trợ lên ý tưởng, viết báo cáo và làm code mẫu. AI giúp mình tổng hợp 5 bài toán, phát triển 3 Quick Problem Cards và phân tích bài toán hỗ trợ tài xế Xanh SM khi pin yếu. Nhờ vậy, mình có bản nháp để xem lại và hoàn thiện từng phần theo yêu cầu của worksheet.

AI cũng hỗ trợ mô tả quy trình hiện tại, so sánh cách dùng rule với LLM và viết các tình huống kiểm tra prompt. Với bài toán này, phần kiểm tra ngưỡng pin có thể dùng rule, còn LLM hỗ trợ đọc tin nhắn và soạn đề xuất. Mọi đề xuất vẫn cần điều phối viên kiểm tra trước khi gửi.

Điểm mình cần chú ý là các con số như 8 phút xử lý mỗi ca hay 60 ca mỗi ngày đều là giả định, chưa có dữ liệu thực tế để xác nhận. Vì vậy, bài làm ghi rõ đây là số liệu minh họa. Tên hành động `dispatch_mobile_charger` cũng cần giải thích rõ là đề xuất hỗ trợ sạc di động, không có nghĩa hệ thống đã điều xe.

Để hạn chế AI trả lời sai, prompt được giới hạn cụ thể hơn: chỉ tạo bản nháp có nhãn `[DRAFT_ONLY]`, không tự gửi tin, không bịa vị trí trạm hoặc thời gian hỗ trợ. Theo quy tắc của bài lab, pin dưới 5% thì đề xuất sạc di động và chờ người duyệt; thiếu thông tin thì chuyển cho điều phối viên xử lý.

Khi chạy thử, ban đầu mình gặp lỗi thiếu thư viện (`ModuleNotFoundError`). Sau khi kiểm tra, thư viện đã được cài trong `.venv` nhưng lệnh chạy lại dùng Python bên ngoài. Mình đổi sang chạy bằng `.venv\Scripts\python.exe` thì phần import thư viện hoạt động được.

Tiếp theo, khi gọi Gemini 2.5 Flash, chương trình báo lỗi `429 RESOURCE_EXHAUSTED`. Thông báo cho biết đã hết quota miễn phí, với giới hạn hiển thị là 20 yêu cầu/ngày. Một lần gọi khác báo lỗi `400 INVALID_ARGUMENT`, yêu cầu dùng API `v1beta` để gửi system instruction. Code đã được sửa để chỉ định `v1beta`, nhưng chưa có kết quả chạy thành công sau lần sửa này.

Qua cách làm này, mình thấy AI giúp tạo bản nháp nhanh hơn, nhưng vẫn cần kiểm tra số liệu, cách diễn đạt và phạm vi được phép làm. Một câu trả lời nghe hợp lý chưa chắc đã đúng với thực tế, nhất là khi bài toán liên quan đến vận hành xe.
