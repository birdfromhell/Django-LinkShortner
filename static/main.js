let text = document.getElementById('shortlink').innerHTML;
  const copyFunction = async () => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
      alert('Text telah Di Copy')
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }