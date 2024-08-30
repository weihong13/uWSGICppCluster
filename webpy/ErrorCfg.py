#-*- encoding:utf-8 -*-

# 错误码


# 通用错误[1-99]
EC_LOGIN_INVALID = 1
ER_LOGIN_INVALID = "请重新登录"

EC_MONEY_NOT_ENOUGH = 2
EC_MONEY_NOT_ENOUGH = "余额不足，请充值"


# 注册错误[100-199]
EC_REGISTER_PHONENUM_TYPE_ERROR = 100
ER_REGISTER_PHONENUM_TYPE_ERROR = "手机号格式错误，请重新输入"


EC_REGISTER_USERID_REPEAT = 101
ER_REGISTER_USERID_REPEAT = "该用户名已被注册，请重新输入"

EC_REGISTER_IDCARD_ERROR = 102
ER_REGISTER_IDCARD_ERROR = "身份证号有误，请重新输入"

EC_REGISTER_PWD_TYPE_ERROR = 103
ER_REGISTER_PWD_TYPE_ERROR = "密码格式有误，请输入8-16位密码（字母、数字、特殊字符：?=.*+!@）"

# 登录错误[200-299]
EC_LOGIN_USERID_ERROR = 200
ER_LOGIN_USERID_ERROR = "账号不存在，请重新输入"

EC_LOGIN_PASSWORD_ERROR = 201
ER_LOGIN_PASSWORD_ERROR = "密码错误，请重新输入"

EC_LOGIN_STATUS_FRERZE = 202
ER_LOGIN_STATUS_FRERZE =  "当前账号已冻结"


# 商城错误[300-399]
EC_SHOP_VERSION_LOW = 300
ER_SHOP_VERSION_LOW = "商城版本过低，请刷新重试"

EC_PROP_NOT_SHOW = 301
ER_PROP_NOT_SHOW = "该商品未上架"

EC_PROP_NOT_EXIST = 302
ER_PROP_NOT_EXIST = "该商品不存在"

EC_PROP_VERSION_LOW = 303
ER_PROP_VERSION_LOW = "客户端版本过低，请更新后重试"

EC_PROP_BUY_LIMIT = 304
ER_PROP_BUY_LIMIT = "超出限购数量，请减少购买数量"

EC_INVENTORY_NOT_ENOUGH = 305
ER_INVENTORY_NOT_ENOUGH = "商品库存不足，请减少购买数量"

EC_SHOP_BUY_MONEY_NOT_ENOUGH = 306
ER_SHOP_BUY_MONEY_NOT_ENOUGH = "购买时余额不足，请先充值"


# 任务错误[400-499]
EC_TASK_NOT_EXIST = 400
ER_TASK_NOT_EXIST = "该任务不存在"

EC_TASK_NOT_FINISH = 401
ER_TASK_NOT_FINISH = "该任务未完成"

EC_TASK_STATE_INVALID = 402
ER_TASK_STATE_INVALID = "当前任务已失效"

EC_TASK_STATE_AWARDED = 403
ER_TASK_STATE_AWARDED = "该任务奖励已领取"

EC_TASK_CLAIM_FAILED = 404
ER_TASK_CLAIM_FAILED = "领取奖励失败，请重试"

EC_TASK_SIGN_TYPE_ERROR = 405
ER_TASK_SIGN_TYPE_ERROR = "签到类型错误"

EC_TASK_SIGN_FINISH = 406
ER_TASK_SIGN_FINISH = "当前日期已完成签到"


# 邮件错误[500-599]
EC_MAIL_INFO_ERROR = 500
ER_MAIL_INFO_ERROR = "邮件信息错误"

EC_MAIL_NOT_EXIST = 501
ER_MAIL_NOT_EXIST = "邮件不存在"
