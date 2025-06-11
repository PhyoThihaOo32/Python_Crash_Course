from admin import Admin
 
admin1 = Admin('Micky', 'Mouse', password= 'babymilo@123')
admin1.privilleges.set_privillages('can_add_post', 'can_delete_post', 'can_ban_user', 'can_block_user')
admin1.describe_user()
admin1.privilleges.show_privilleges()