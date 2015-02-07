# -*- coding: utf-8 -*-
from livesettings import config_register, ConfigurationGroup, PositiveIntegerValue, PercentValue, StringValue
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
MYAPP_GROUP = ConfigurationGroup(
    'MyApp',               # key: internal name of the group to be created
    u'Настройки сайта',  # name: verbose name which can be automatically translated
    ordering=0             # ordering: order of group in the list (default is 1)
    )



config_register(StringValue(
                            MYAPP_GROUP,
        'EMAIL', 
        description = u'Email администратора',
        help_text = u"Почта, куда будут приходить заявки.",
        default = 'annkpx@gmail.com'
    ))

config_register(StringValue(
                            MYAPP_GROUP,
        'PHONE', 
        description = u'Телефон',
        help_text = u"Для отображения на сайте",
        default = '8 (926) 555-55-55'
    ))

config_register(StringValue(
                            MYAPP_GROUP,
        'ORDERS_COUNT', 
        description = u'Кол-во заказов выполненных',
        help_text = u"Для отображения в шапке сайта",
        default = '986'
    ))