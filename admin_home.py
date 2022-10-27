from fun import *
class Take():

    name =None
    username= None
    roll = None
    img = None
    contact = None
    year = None
    group = None
    dept = None
    password = None
    language = list(get_lang('Username'))
    working = None
    score = None
    message = None
    acceptance = None
    def give(self,user):
        use = log_in_user(user)
        member = quary_user(user)
        m_score = quary_rate(user)
        m_notf = qur_notif(user)
        self.username = member.username
        self.name = member.name
        self.roll = member.roll
        self.img =member.img
        self.contact = member.contact
        self.year = member.year
        self.group = member.group
        self.password = use.password
        self.language = list(get_lang(user))
        self.working = quary_ability(user)
        self.score = m_score.rate
        self.message = m_notf.message
        self.acceptance = m_notf.acceptance
    def get_name(self):
        return self.username
    def get_year(self):
        return self.year