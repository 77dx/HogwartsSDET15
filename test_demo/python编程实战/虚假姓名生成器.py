"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/6 11:43
"""
import random

# 拿到题目后，参考之前的代码写的答案
def generateName():
    print("Welcome")
    xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩',
            '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏',
            '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚',
            '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗',
            '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余',
            '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹']
    ming = ['梦琪', '忆柳', '之桃', '慕青', '问兰', '元香', '初夏', '沛菡', '傲珊', '曼文', '乐菱', '痴珊',
            '恨玉', '惜文', '香寒', '新柔', '妹子', '海安', '夜蓉', '涵柏', '水桃', '醉蓝', '春儿', '语琴',
            '从彤', '傲晴', '语兰', '又菱', '碧彤', '元霜', '怜梦', '紫寒', '妙彤', '曼易', '南莲', '紫翠',
            '雨寒', '易烟', '如萱', '若南', '寻真', '晓亦', '野孩', '彬翎', '君毅', '晋月', '彬翰', '泽君',
            '彬杰', '松霖', '圣棋', '松明', '浩凯', '旭皓', '江杉', '亦君', '圣毅', '柏枝', '观云', '棋圣',
            '贤达', '玮业', '浩楷', '野松', '展毅', '圆滑', '龙菲', '世奇', '星柯', '志元', '强志', '杰雄',
            '杰鸿', '晋毅']

    while True:
        name = random.choice(xing) + random.choice(ming)
        print(name)
        content = input("Try again？(Press Enter else n to quit):")
        if content == "n":
            break


if __name__ == '__main__':
    generateName()
