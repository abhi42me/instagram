from model.channel import Channel
from model.user import User
from model.channel_subscription import ChannelSubscription
from model.image import Image
from data_layer.daos import user_dao, image_dao, channel_subscription_dao, channel_dao
from services.timeline_service import TimeLineService

user1 = User("Abhishek")
user_dao.save(user1)

user2 = User("Sachin")
user_dao.save(user2)

user3 = User("Vivek")
user_dao.save(user3)

user1_channel1 = Channel("channel_u1_1", user1.id)
channel_dao.save(user1_channel1)
user1_channel2 = Channel("channel_u1_2", user1.id)
channel_dao.save(user1_channel2)

image1 = Image("/user/1/path/1", user1.id, user1_channel1.id)
image_dao.save(image1)

image2 = Image("/user/1/path/2", user1.id, user1_channel2.id)
image_dao.save(image2)

channel_subscription_dao.save(ChannelSubscription(user1_channel1.id, user2.id))
channel_subscription_dao.save(ChannelSubscription(user1_channel2.id, user2.id))

channel_subscription_dao.save(ChannelSubscription(user1_channel2.id, user3.id))

timeline_user2 = TimeLineService.generate_timeline(user2.id)
print(timeline_user2)
timeline_user3 = TimeLineService.generate_timeline(user3.id)
print(timeline_user3)
