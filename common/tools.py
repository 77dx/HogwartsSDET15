import datetime
import os.path

# import ddddocr


def get_now_time():
    return datetime.datetime.now()


def get_now_date_str():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_project_path() -> str:
    """
    获取项目的绝对路径
    :return:
    """
    project_name = "HogwartsSDET15"
    # 获取当前模块的绝对路径
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False) -> str:
    """
    使用分隔符拼接任意数量的字符
    :param path: 路径列表，类型为列表
    :param add_sep_before: 是否需要在拼接的路径前加一个分隔符
    :param add_sep_after: 是否需要在拼接的路径后加一个分隔符
    :return: 完整路径
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path += os.sep
    return all_path


def get_img_path(img_name, contain_subdirectory=False, subdirectory=None):
    """
    获取本地目录下存放的商品图片路径
    :param img_name: 图片名称
    :param contain_subdirectory: 是否包含子目录
    :param subdirectory: 子目录名称
    :return:
    """
    project_path = get_project_path()
    img_dir = project_path
    if contain_subdirectory:
        for dir_name in subdirectory:
            img_dir = sep([img_dir, dir_name])
        return sep([img_dir, img_name])
    return sep([project_path, img_name])

# 可能是版本问题，import报错
# def ocr_identify(pic_path):
#     ocr = ddddocr.DdddOcr()
#     image = None
#     with open(pic_path, "rb") as f:
#         image = f.read()
#     res = ocr.classification(image)
#     return res



def delete_logs():
    """
    由于log的数量实在太多，就手动删除一下
    :return:
    """
    # 获取log所在目录的所有日志文件
    log_path = os.path.join(get_project_path(), 'logs/autotest_web_logs')
    log_list = os.listdir(log_path)
    for i in log_list[:-5]:
        os.remove(os.path.join(log_path, i))
    print("It was done")


if __name__ == '__main__':
    delete_logs()













