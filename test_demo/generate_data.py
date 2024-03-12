"""
@ Title:
@ Author: Cathy
@ Time: 2023/12/20 11:21
"""
from common.mysql_operate import MysqlOperate
from cn2an import an2cn
import random
class GenarateData:

    # 生成1年级1班到10班，直到高3,10班
    def grade_data(self):
        grades = []
        # 年级
        for i in range(1,13):
            # 班级
            for j in range(1,10):
                grade_num = an2cn(i, "direct")
                class_num = an2cn(j, "direct")
                if i == 7:
                    grade_num = "初一"
                elif i == 8:
                    grade_num = "初二"
                elif i == 9:
                    grade_num = "初三"
                elif i == 10:
                    grade_num = "高一"
                elif i == 11:
                    grade_num = "高二"
                elif i == 12:
                    grade_num = "高三"
                grades.append(grade_num+"年级"+class_num+"班")
        return grades

    # 生成目标为： insert into grade (school_id, grade_name) values(1,'一年级一班')，(1,'一年级二班')
    def insert_grade(self):
        grade_list = self.grade_data()
        sql = 'insert into grade (school_id, grade_name) values'
        for i in grade_list:
            sql = sql + '(1, "'+i+'"),'
        return sql

    """
    很遗憾，上面两个方法都没有使用了，原因是需求理解错了，在实际操作的时候才发现。
    """

    # 想要自己生成一些姓名
    def generate_student_name(self):
        str_surname = '赵、钱、孙、李、周、吴、郑、王、冯、陈、褚、卫、蒋、沈、韩、杨、朱、秦、尤、许、何、吕、施、张、孔、曹、严、华、金、魏、陶、姜、戚、谢、邹、喻、柏、水、窦、章、云、苏、潘、葛、奚、范、彭、郎、鲁、韦、昌、马、苗、凤、花、方、俞、任、袁、柳、酆、鲍、史、唐、费、廉、岑、薛、雷、贺、倪、汤、滕、殷、罗、毕、郝、邬、安、常、乐、于、时、傅、皮、卞、齐、康、伍、余、元、卜、顾、孟、平、黄、和、穆、萧、尹'
        list_surname = str_surname.split('、')
        str_second_name = '梦琪、忆柳、之桃、慕青、问兰、元香、初夏、沛菡、傲珊、曼文、乐菱、痴珊、恨玉、惜文、香寒、新柔、妹子、海安、夜蓉、涵柏、水桃、醉蓝、春儿、语琴、从彤、傲晴、语兰、又菱、碧彤、元霜、怜梦、紫寒、妙彤、曼易、南莲、紫翠、雨寒、易烟、如萱、若南、寻真、晓亦、野孩、彬翎、君毅、晋月、彬翰、泽君、彬杰、松霖、圣棋、松明、浩凯、旭皓、江杉、亦君、圣毅、柏枝、观云、棋圣、贤达、玮业、浩楷、野松、展毅、圆滑、龙菲、世奇、星柯、志元、强志、杰雄、杰鸿、晋毅'
        list_second_name = str_second_name.split('、')

        # insert into student (class_id, student_name,birthday,sex) VALUES (1,"赵水桃",'1998-01-12',0)
        sql = 'insert into student (class_id, student_name,birthday,sex) VALUES '
        for i in range(1,31):
            student_name = random.choice(list_surname) + random.choice(list_second_name)
            sql = sql+'('+str(i)+',"'+student_name+'","1999-09-09",'+str(random.randint(0,1))+'),'
        return sql.rstrip(',')+";"

    # 插入学生数据，由于一个学生只能属于一个班级，所以插入之前要查询该学生所属班级的年级的科目都有哪些，然后再逐个插入
    # insert into score (student_id, course_id, score) VALUES (2,1,75),(2,2,44),(2,3,65),(2,4,67),(2,5,87);
    def insert_student_score(self):
        sql = 'insert into score (student_id, course_id, score) VALUES'
        for i in range(3,92):
            select_sql = 'SELECT id from course WHERE grade_id = (SELECT grade_id from class WHERE id=(SELECT class_id from student WHERE id = %s));' %i
            result = MysqlOperate().query(select_sql)
            print(result)
            # 拼接sql语句
            for m in result:
                course_id = m[0]
                sql = sql + '(%s,%s,%s),'%(i, course_id, random.randint(0, 100))
        sql = sql.rstrip(',')+';'
        print(sql)
        # MysqlOperate().query(sql)




















if __name__ == '__main__':
    g = GenarateData()
    g.insert_student_score()





