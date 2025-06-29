from storage_service import StorageService
from recognition_service import RecognitionService

storageService = StorageService()
recognitionService = RecognitionService()

bucket_name = 'com.sagar.recognitionimages'

for file in storageService.get_all_files(bucket_name):
    if file.key.endswith('jpg') or file.key.endswith('png'):
        print('Object detected in image' + file.key + ':')
        ##response = recognitionService.detect_objects(file.bucket_name, file.key)
        response = recognitionService.detect_moderation_labels(file.bucket_name, file.key)
        if len(response['ModerationLabels']) == 0 :
            print('None')
        for label in response['ModerationLabels']:
            print(' ->  ' + label['Name'] + ': ' + str(label['Confidence']))
