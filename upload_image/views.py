from django.shortcuts import render
from forms import ImageUploadForm
from models import ImageModel
# Create your views here.
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image=ImageModel(image = request.FILES['image'])
            image.save()
            return render(request, 'success.html')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

