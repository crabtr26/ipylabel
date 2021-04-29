import pandas as pd
import ipywidgets as widgets
from ipylabel.templates import Table


class ImageDashboard():
    '''
    Abstract dashboard class for image data.
    '''
    
    def __init__(self, images, format='png'):
        if format not in ['png', 'jpg']:
            raise ValueError('Format must be either png or jpg')
        self.image_format = format
        self.images = self.generate_ipyimages(images=images)
        self.figure = self.generate_figure()
        
    def generate_ipyimages(self, images):
        '''
        Create an ipywidgets.Image object for each image.
        
        Args:
            images (list): A list of image bytes objects.
            
        Returns:
            ipyimges (list): A list of ipywidgets.Image objects.
            
        '''
           
        if isinstance(images, list):
            try:
                ipyimages = []
                for image in images:
                    assert isinstance(image, bytes)
                    ipyimage = widgets.Image(value=image, format=self.image_format)
                    ipyimages.append(ipyimage)
                return ipyimages
            except AssertionError as e:
                raise ValueError(f'images parameter must contain a list of image bytes objects.') from e
                
        else:
            raise ValueError(f'images parameter must contain a list of image bytes objects.')
            
class ImageClassification(ImageDashboard):
    
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        self.table = generate_table()
        
    def generate_table(self):
        df = pd.DataFrame([1])
        return Table(data=df, title='Labels')
    
    