from whoiscristo.models import CristoPoll, Choice, Vote, User


def get_current_poll():
    """
    :return: CristoPoll
    """
    return CristoPoll.objects.latest('pub_date')


def get_last_finished_poll():
    order_by = 'pub_date'
    assert bool(order_by), "earliest() and latest() require either a " \
                           "field_name parameter or 'get_latest_by' in the model"
    assert CristoPoll.objects.query.can_filter(), \
        "Cannot change a query once a slice has been taken."
    obj = CristoPoll.objects._clone()
    obj.query.set_limits(high=2)
    obj.query.clear_ordering(force_empty=True)
    obj.query.add_ordering('%s%s' % ("-", order_by))
    return obj.get()[1]
