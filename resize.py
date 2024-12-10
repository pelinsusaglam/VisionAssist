import cv2

# Video dosyasının yolu
video_path = "kampus.mp4"


cap = cv2.VideoCapture(video_path)


new_width = 640
new_height = 640
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("kampus.mp4", fourcc, 30, (new_width, new_height))

# Başlangıç zamanını ayarla
start_time = 10  # İlk 20 saniyeyi atla

# Başlangıç zamanına kadar okuma yap
while cap.get(cv2.CAP_PROP_POS_MSEC) < start_time * 1000:
    ret, frame = cap.read()

while True:
    # Video'dan bir frame oku
    ret, frame = cap.read()
    if not ret:
        break
    
    # Frame boyutlarını değiştir
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Yeniden boyutlandırılmış frame'i kaydet
    out.write(resized_frame)

    # Yeniden boyutlandırılmış frame'i göster
    cv2.imshow('Resized Frame', resized_frame)
    
    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kullanılan kaynakları serbest bırak
cap.release()
out.release()
cv2.destroyAllWindows()

