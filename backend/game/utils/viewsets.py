from rest_framework import viewsets


class ViewSetBase(viewsets.ModelViewSet):
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(ViewSetBase, self).get_serializer_class()

