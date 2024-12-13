import speedtest

def test_speed():
    st = speedtest.Speedtest()
    print("Test server...")
    st.get_best_server()
    print("Download speed...")
    download_speed = st.download() / 1_000_000 # Convert to Mbit/s
    print('Speed download: {:.2f} mbit/s'.format(download_speed))

if __name__=="__main__":
    test_speed()