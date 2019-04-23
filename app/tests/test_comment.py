from app.models import Commnet,User
from app import db


def setUp(self):
        self.user_Rotich = User(username = 'Rotich',password = 'potato', email = 'rotichtitus12@gmail.com')
        self.new_comment = Comment(pitch_title='Comment for pitchs',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",pitch_comment='This pitch is the best thing since sliced bread',user = self.user_Rotich )

def tearDown(self):
        Comment.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_title,'Comment for pitches')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.pitch_comment,'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_Comment.user,self.user_Rotich)

def test_get_Comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)