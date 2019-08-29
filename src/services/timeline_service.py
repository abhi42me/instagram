from data_layer.daos import user_dao, image_dao, channel_dao, channel_subscription_dao

class TimeLineService(object):

    # TODO
    # start, limit
    @staticmethod
    def generate_timeline(user_id):
        channel_ids = channel_subscription_dao.get_user_subscriptions(user_id)
        timeline_images = []
        for channel_id in channel_ids:
            image_ids = channel_dao.get_top_channel_images(channel_id, 10)
            timeline_images += image_ids

        return timeline_images
