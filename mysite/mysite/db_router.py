#
# class BlackmoresRouter:
#     """
#     A router to control blackmores application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read blackmores models go to blackmores_db.
#         """
#         if model._meta.app_label == 'blackmores':
#             return 'blackmores_db.sqlite3'
#         return None
#
#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write blackmores models go to auth_db.
#         """
#         if model._meta.app_label == 'blackmores':
#             return 'blackmores_db.sqlite3'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the blackmores app is involved.
#         """
#         if obj1._meta.app_label == 'blackmores' or \
#            obj2._meta.app_label == 'blackmores':
#            return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the blackmores app only appears in the 'blackmores_db'
#         database.
#         """
#         if app_label == 'blackmores':
#             return db == 'blackmores_db.sqlite3'
#         return None