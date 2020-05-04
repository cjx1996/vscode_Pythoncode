from distutils.core import setup

setup(name="wk_message",  # 包名
      version="1.0",  # 版本
      description="发送信息和接收信息模块",
      long_description="完整的描述信息",
      author="作者",
      author_email="作者邮箱",
      url="主页",
      py_modules=["wk_message.send_message",
                  "wk_message.receive_message"])