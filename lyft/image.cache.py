import fileinput
import hashlib
import urllib.request
import io


def run():
    i = 0
    cache = {}
    cache_size_bytes = number_of_urls = ''
    total_size = 0
    for line in fileinput.input():
        if i == 0:
            cache_size_bytes = int(line)
        elif i == 1:
            number_of_urls = int(line)
        else:
            url = line.rstrip()
            h = hashlib.md5(url.encode('utf-8')).hexdigest()

            if h not in cache:
                status = 'DOWNLOADED'

                image, size = download(url)
                if total_size + size > cache_size_bytes:
                    total_size = drop_last_used_items(cache, total_size, size, cache_size_bytes)
                cache[h] = image, size
            else:
                status = 'IN_CACHE'
                image, size = cache[h]
                del cache[h]
                cache[h] = image, size

            total_size += size
            print("%s %s %d %d %s" % (url, status, size, total_size, h[-1]))

        i += 1
        j = 0
        for k in cache.keys():
            print(j, k[-1])
            j += 1

    print('cache_size_bytes =', cache_size_bytes)
    print('number_of_urls = ', number_of_urls)
    print('total_size =', total_size)


def download(url):
    img = urllib.request.urlopen(url)
    size = 0
    content = io.BytesIO()
    while True:
        bt = img.read(1)
        if len(bt) < 1:
            break
        size += len(bt)
        content.write(bt)

    # print(size, 'characters written')
    return content, size


def drop_last_used_items(cache, total_size, size_to_add, cache_size_bytes):
    if not len(list(cache)):
        return total_size
    key = list(cache)[0]
    _, size = cache[key]
    del cache[key]
    total_size -= size
    print('removed one')
    if total_size + size_to_add > cache_size_bytes:
        print('try to remove more')
        drop_last_used_items(cache, total_size, size_to_add, cache_size_bytes)
    return total_size

run()
