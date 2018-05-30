第0000题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

获取QQ空间头像方法：
小图
http://qlogo.store.qq.com/qzone/[QQ号]/[QQ号]/50
中图
http://qlogo.store.qq.com/qzone/[QQ号]/[QQ号]/100
大图
http://qlogo.store.qq.com/qzone/[QQ号]/[QQ号]/640
获取QQ头像接口
大图
http://q.qlogo.cn/g?b=qq&nk=[QQ号]&s=640&mType=friendlist
http://q.qlogo.cn/g?b=qq&k=[加密后的22位QQ号]&s=640&mType=friendlist
静态小图
http://q.qlogo.cn/g?b=qq&nk=[QQ号]&s=100&mType=QQHeadIcon&t=[当前时间的整数]
http://q.qlogo.cn/g?b=qq&k=[加密后的22位QQ号]&mType=QQHeadIcon&t=[当前时间的整数]

python知识点
sys.path[0]获取脚本的位置
sys.argv[0]获取脚本执行时的路径
__file__同sys.argv[0]
os.path.abspath(__file__)获取脚本本身的绝对路径
