from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/truth')
def get_truth():
    truths = [
        
"Nếu bạn có khả năng tàng hình trong 1, bạn sẽ làm gì",
        "Nói 3 điều bạn muốn crush làm với bạn",
        "Crush của bạn là ai",
        "Giới hạn độ tuổi mà bạn muốn yêu là bao nhiêu? Vì Sao?",
        "Bạn muốn trở thành người như thế nào khi lớn lên",
        " Đọc to những gì bạn tìm kiếm trên Google điện thoại gần nhất",
        "Nếu được hoán đổi cuộc sống với một người ở đây thì bạn sẽ chọn ai",
        "Kể về lần bạn đã lừa đảo hoặc bị lừa đảo",
        "kể tên 10 việc bạn nhất định phải làm trước khi ngỏm",
        "Kể về lần say xỉn nhất của bạn",
        "kể về khoảng khắc xấu hổ nhất của bạn khi ở trường học",
        "con số hay điều gì mà bạn tin rằng nó sẽ may mắn cho bạn ?",
        "Kể về một điều điên rồ nhất mà bạn đã làm để thoát khỏi giấy phạt của CSGT",
        "Bạn đã bao giờ hẹn hò với ai đó chỉ vì tình dục?",
        "Bạn đã từng Stalk ai trên mạng xã hội chưa ? Nói ngay đây là ai nàooo?",
        "Mở máy lên và nói bạn nhắn tin với ai nhiều nhất",
        "Kể một điều mà người khác thường đánh giá sai về bạn",
        "Chia sẻ về trải nghiệm 'tự làm bản thân phê' kì lạ nhất",
        "Ai là người trong nhóm từng khiến bạn buồn nhất? Vì sao?",
        "Sắp xếp mọi người theo thứ tự từ thích nhiều đến ít nhất!",
        "Ai là người cướp đi nụ hôn đầu của bạn",
        "Bạn làm gì đầu tiên khi biết mình bị cắm sừng",
        "Thói quen/ hành động gì ở đối phương khiến bạn lập tức 'say bye' vì sao ?",
        "cảm thấy mình khó thân thiết với ai nhất trong nhóm",
        "Một điều mà bạn nghĩ mọi người trong nhóm nên thử",

        "Bạn sẽ chọn ai trong nhóm, để cùng xem 'phim con lợn' cùng bạn ?",
        "Tin đồn thất thiệt nhất mà bạn từng nghe về bản thân là gì ?",
        "Mối tình đơn phương lâu nhất của bạn là bao lâu?",
        "Hành động bất thường nhất mà bạn từng làm trong toilet là gì ?",
        "Kể về hành động của một người mà làm bạn ghét cay, ghét đắng",
        # Thêm câu hỏi "Truth" khác nếu bạn muốn
    ]
    return random.choice(truths)

@app.route('/dare')
def get_dare():
    dares = [
             
         "Chọn người t4 trong list member và thả thính họ",
        "Đổi avatar Facebook public người yêu/crush của bạn",
        "Mở History 1 tuần gần đây của bất kì ứng dụng cho mọi người xem đi",
        "Khoe bên trong túi xách/ ví của bạn cho mọi người cùng xem",
        "Kể về lần mất tiền ngu nhất của bạn",
        " kêu quắc quắc như con vịt cho đến lượt tiếp theo của bạn",
        "Mở IG or FB của ngừi êu cũ/crush và like toàn bộ bài viết của họ",
        "Hét to bất cứ câu nào bạn muốn",
        "Bạn phải thay đổi nguyên âm 'nh' cho câu nói trong 10 phút",
        "Nhắn tin cho người bạn thích và hẹn họ đi chơi",
        "Trả lời 5 lần 'tất nhiên rồi' x5 khi người khác hỏi bạn",
        "'Bão tim' các bài đăng (>20 bài đăng) của một người bạn bất kì trên IG",
        "Thè lưỡi ra và nói chuyện trong vòng 2 lượt tiếp theo",
        "Bắt chước 1 người nổi tiếng mỗi khi bạn nói chuyện",
        
        "Diễn tả 3 điều bạn muốn crush làm với bạn",
        "chụp selfie với một người chơi khác và đăng story với caption 'Mình cưới bạn này nha'",
        "Hô tên người chơi mà bạn cho là xấu nhất và bạn phải lì xì cho họ 20k",
        
   
        "hãy nhai một đống giấy (giấy ăn/ giấy tờ) vào mồm",
        "Giả làm tiếng sói tru thật lớn 3 lần",
        "Kêu tất cả im lặng rồi rên lên cho đến khi có một người bật cười",
        "Mũi chạm mũi một người bất kì trong nhóm",
        "Xưng hô mọi người bằng cách gọi đầy đủ họ và tên. Phạt bị búng tai 3 cái nếu vi phạm",
        "Xoá kết bạn với 3 người bạn bất kì đang có mặt ở đây",
        "Kể tên 10 web phim người lớn' mà bạn từng truy cập",
        "Hãy đăng story: 'Muốn kết hôn mà không cần rửa đít'",
        "Kêu 'meow meow meow' thay cho lời bạn nói cho đến lượt tiếp theo của bạn",
        "Lặp lại tất cả những gì người bên phải bạn làm cho đến lượt tiếp theo của bạn",
        
        "Gọi 1 người bất kì và thả thính họ",
        "tất cả mọi người phải thả thính bạn và bạn chọn ra người thả thính giỏi nhất",
        "Thay đổi xưng hô 'Tui-Mấy ní' cho đến hết trò chơi, phạt hít đất 3 cái nếu vi phạm",
        "Nắm tay một người do bạn bè chọn 5p",
        "Từng người nói 1 từ theo thứ tự, bạn sẽ ghi lại những từ đó và đăng lên mxh",
        "Năn nỉ xin 1 ng bất kỳ 100k",
        "Hãy sủa như 1 con cún đi",
        
        "Gửi hôn gió đến tất cả mọi người",
        # Thêm thách thức "Dare" khác nếu bạn muốn
    ]
    return random.choice(dares)

if __name__ == '__main__':
    app.run(debug=True)
