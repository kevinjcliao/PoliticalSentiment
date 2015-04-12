from indicoio.utils import is_url

def test_is_urls():
    boring_image = [0]*(32**2)
    boring_images = [boring_image]*100

    assert not is_url(boring_image, batch=False)
    assert not is_url(boring_images, batch=True)

    url = 'http://picturepicture.com/picture'
    urls = [url]*100

    assert is_url(url, batch=False)
    assert is_url(urls, batch=True)

