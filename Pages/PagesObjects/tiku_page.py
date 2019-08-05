from Pages.PagesObjects.basepage import BasePage
class TiKuPade(BasePage):

    # 随机选择一个题库类型，然后点进去
    def select_tiku_type(self):
        # 获取所有的题库类型--翻译。需要获取每个页面的题库类型
        # 放在一个大的列表当中，去重
        # 在随机选取题库类型名字，然后再去操作
        pass

    #选择题库等级：初中高
    def select_topic_level_by_name(self):
        pass

    # 选择套题，如何选，随机，选第一个，选最近一个
    def select_topic_suit(self):
        pass

    # 收藏开头
    def switch_favorite(self,action="False"):
        pass

        # 题目开关

    def switch_answer(self, action="False"):
        pass

    #拉动题目
    def switch_full(self):
        pass
