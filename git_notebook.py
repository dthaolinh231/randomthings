# ============================================
# GIT NOTEBOOK – LUỒNG LÀM VIỆC CƠ BẢN
# File này dùng để bạn thực hành Git trong VS Code
# - Sửa code
# - git add
# - git commit
# - git push / git pull
# ============================================

# 1. CÁC KHÁI NIỆM CƠ BẢN (ÔN LẠI)
# --------------------------------
# Working tree (working directory):
#   - Thư mục hiện tại bạn đang mở trong VS Code
#   - Nơi file thật nằm (bạn đang gõ code, sửa file)
#
# Staging area:
#   - Nơi chứa các thay đổi đã "chọn" để commit
#   - git add = đưa file từ working tree -> staging area
#
# Local repository (repo local):
#   - Nằm trong thư mục ẩn .git
#   - Lưu lịch sử commit, branch...
#
# Remote repository:
#   - Repo trên GitHub/GitLab/Bitbucket...
#   - Nơi bạn push code lên và pull code về
#
# Lệnh hay dùng:
#   - git status    -> xem trạng thái
#   - git add .     -> đưa toàn bộ thay đổi vào staging
#   - git commit -m "message"   -> tạo snapshot (commit)
#   - git push      -> đẩy commit lên remote (GitHub)
#   - git pull      -> lấy commit mới từ remote về máy
#
# Ghi nhớ hướng:
#   - PUSH: Local  -> Remote
#   - PULL: Remote -> Local


# 2. LUỒNG CÔNG VIỆC CƠ BẢN
# --------------------------------
# Mỗi lần bạn muốn cập nhật code:
#
#   Bước 1: git pull
#       -> Lấy code mới nhất từ remote về
#
#   Bước 2: Sửa code trong VS Code (file này chẳng hạn)
#
#   Bước 3: git status
#       -> Xem file nào bị Modified / Untracked
#
#   Bước 4: git add <file> hoặc git add .
#
#   Bước 5: git commit -m "mô tả ngắn gọn"
#
#   Bước 6: git push
#
# Bạn có thể dùng file này để luyện:
#   - Sửa 1 dòng -> add -> commit -> push
#   - Sửa tiếp 1 dòng -> add -> commit -> push


# 3. MỘT TÍ CODE ĐỂ BẠN THỰC HÀNH SỬA
# ------------------------------------

def say_hello(name: str) -> str:
    """
    Hàm đơn giản để bạn sửa nhiều lần rồi commit.

    TODO:
    - Lần 1: Đổi message trả về.
    - Lần 2: Thêm số lần chào.
    - Lần 3: Thêm logic if/else.

    Mỗi lần sửa:
        git status
        git add git_notebook.py
        git commit -m "Mô tả lần sửa"
        git push
    """
    return f"Hello, {name}! Đây là version 2 từ branch testing."



# BÀI TẬP GỢI Ý CHO BẠN:
# ------------------------------------
# 1) Lần đầu:
#    - Chạy hàm, ví dụ trong Python REPL:
#          >>> from git_notebook import say_hello
#          >>> say_hello("Linh")
#    - Sửa nội dung return, ví dụ:
#          return f"Xin chào {name}, đây là bản 2!"
#    - Rồi:
#          git add git_notebook.py
#          git commit -m "Update message say_hello v2"
#          git push
#
# 2) Lần sau:
#    - Thêm tham số count để chào nhiều lần:
#
#       def say_hello(name: str, count: int = 1) -> str:
#           messages = []
#           for i in range(count):
#               messages.append(f"{i+1}. Hello, {name}!")
#           return "\n".join(messages)
#
#    - Rồi tiếp tục add/commit/push.
#
# 3) Bạn có thể thêm hàm mới:
#
#    def add(a: int, b: int) -> int:
#        return a + b
#
#    -> Commit: "Add add() function"
#
# Mục tiêu:
#   - Bạn quen cảm giác: sửa file -> git status -> add -> commit -> push
#   - Hiểu rõ: code chỉ lên GitHub khi bạn commit + push.
#

if __name__ == "__main__":
    # Bạn có thể chạy file này bằng:
    #   python git_notebook.py
    #
    # Và thay đổi nội dung dưới mỗi lần commit để luyện tập.
    print(say_hello("Thế giới"))
