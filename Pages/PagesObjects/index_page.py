from Pages.PagesObjects.basepage import BasePage
class IndexPade(BasePage):
    pass

    #切换导航
    def switch_nav(self,nav_name):
        #根据导航名称切换
        ele_loc = 'new UiSelector().text("{}")'.format(nav_name)
        #先等待在切换
        self.click_element()
