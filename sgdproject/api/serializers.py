from rest_framework import serializers
from .models import Category, CollectionCenter, Provider, ProviderContact, Donation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'state', 'createdAt', 'createdBy') #Delete field to not show

class CollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCenter
        fields = ('id', 'name', 'address', 'latitude', 'longitude', 'state', 'createdAt', 'createdBy')

class ProviderContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProviderContact
		fields = ('firstName', 'lastName', 'phoneNumer', 'social', 'provider', 'state', 'createdAt', 'createdBy')

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    #donationList = CategorySerializer(read_only=True, many=True)
    #contacts = ProviderContactSerializer(source='providercontact_set', many=True)
    contacts = ProviderContactSerializer(many=True, read_only=True)
    class Meta:
        model = Provider
        fields = ('businessName', 'address', 'phoneNumer', 'email', 'contacts', 'state', 'createdAt', 'createdBy')
		
class DonationSerializer(serializers.HyperlinkedModelSerializer):
    provider = ProviderSerializer()
    category = CategorySerializer()
    collectionCenter = CollectionCenterSerializer()
    photo_url = serializers.SerializerMethodField('get_photo_url')
    class Meta:
        model = Donation
        fields = ('provider', 'category', 'description', 'collectionCenter', 'beginDate', 'expirationDate', 'photo', 'photo_url', 'state', 'createdAt', 'createdBy')
    
    def get_photo_url(self, obj):
        return obj.photo.url