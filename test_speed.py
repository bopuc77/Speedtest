import speedtest

def test_speed():
    st = speedtest.Speedtest()
    print("Test server...")
    st.get_best_server()
    print("Download speed...")
    print("Upload speed...")
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping
    print(f'Speed download: {download_speed / (2 ** 20)} mb/s')
    print(f'Speed upload: {upload_speed / (2 ** 20)} mb/s')
    print(f'Ping: {ping} m/s')

if __name__=="__main__":
    test_speed()
