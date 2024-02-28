function copyToClipboard() {
            var shortUrl = document.getElementById('shortUrl');
            shortUrl.select();
            document.execCommand('copy');
            alert('Shortened URL copied to clipboard!');
        }
function validateURL() {
            var urlInput = document.getElementById('url');
            var url = urlInput.value.trim();
            var urlPattern = /^(ftp|http|https):\/\/[^ "]+$/;

            if (urlPattern.test(url)) {
                urlInput.classList.remove('invalid');
                urlInput.classList.add('valid');
            } else {
                urlInput.classList.remove('valid');
                urlInput.classList.add('invalid');
            }
        }