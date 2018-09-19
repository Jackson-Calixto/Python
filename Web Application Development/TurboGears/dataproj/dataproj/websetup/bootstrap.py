# -*- coding: utf-8 -*-
"""Setup the dataproj application"""
from __future__ import print_function, unicode_literals
import transaction
from dataproj import model


def bootstrap(command, conf, vars):
    """Place any commands to setup dataproj here"""
    c1 = model.car()
    c1.make = 'Suzuki'
    c1.model = 'Grand Vitara'
    c1.year = 2013
    c1.transmission = 'Automatic'

    c2 = model.car()
    c2.make = 'Jeep'
    c2.model = 'Sahara'
    c2.year = 2016
    c2.transmission = 'Manual'

    model.DBSession.add(c1)
    model.DBSession.add(c2)
    model.DBSession.flush()
    transaction.commit()

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = 'manager'
        u.display_name = 'Example manager'
        u.email_address = 'manager@somedomain.com'
        u.password = 'managepass'

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = 'managers'
        g.display_name = 'Managers Group'

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = 'manage'
        p.description = 'This permission gives an administrative right'
        p.groups.append(g)

        model.DBSession.add(p)

        u1 = model.User()
        u1.user_name = 'editor'
        u1.display_name = 'Example editor'
        u1.email_address = 'editor@somedomain.com'
        u1.password = 'editpass'

        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, '
              'it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.auth>
