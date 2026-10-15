
import streamlit as st
import streamlit.components.v1 as components

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="TALASH AI | Smart Vision",
    page_icon="🛡️",
    layout="wide"
)

# ================= ANIMATED UI =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

.stApp {
    background:
      radial-gradient(ellipse at top left,#142c50,transparent 45%),
      radial-gradient(ellipse at bottom right,#10352f,transparent 40%),
      #070b14;
    color: #e8f0ff;
    font-family: Inter, sans-serif;
}
.block-container {max-width:1400px;padding-top:2rem}
h1,h2,h3,p,label {color:#e8f0ff}
section[data-testid="stSidebar"] {
    background:#0b1322;
    border-right:1px solid #24364e;
}
.hero {
    padding:26px;
    border:1px solid #28566b;
    border-radius:22px;
    background:linear-gradient(120deg,#10233b,#0c1927,#102f30);
    background-size:200% 200%;
    animation:gradient 8s ease infinite;
    margin-bottom:20px;
}
.hero-title {
    font-size:clamp(30px,5vw,48px);
    font-weight:800;
    letter-spacing:3px;
    background:linear-gradient(90deg,#fff,#00e5ff,#00ffa3);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation:glow 3s infinite alternate;
}
.hero-sub {color:#a9c0d9;font-size:13px;letter-spacing:1px}
.card {
    background:linear-gradient(140deg,#142137,#0b1422);
    border:1px solid #273c55;
    border-radius:16px;
    padding:20px;
    animation:fadeup .7s ease both;
    transition:.25s;
}
.card:hover {
    transform:translateY(-4px);
    border-color:#00e5ff;
    box-shadow:0 8px 25px #00e5ff18;
}
.metric-label {font-size:12px;color:#91a9c5;letter-spacing:1px}
.metric-value {font-size:27px;font-weight:800;margin-top:8px}
.note {
    background:#101b2b;
    border:1px solid #28425b;
    padding:15px;
    border-radius:12px;
    color:#bdcfe4;
}
.stButton>button {
    background:linear-gradient(90deg,#00d9f5,#00e6a0);
    color:#06121b;
    border:0;
    border-radius:10px;
    font-weight:800;
    transition:.2s;
}
.stButton>button:hover {
    transform:translateY(-2px);
    box-shadow:0 0 20px #00e5ff55;
    color:#06121b;
}
@keyframes gradient {
    0%,100% {background-position:0% 50%}
    50% {background-position:100% 50%}
}
@keyframes glow {
    from {filter:drop-shadow(0 0 1px #00e5ff)}
    to {filter:drop-shadow(0 0 12px #00e5ff66)}
}
@keyframes fadeup {
    from {opacity:0;transform:translateY(12px)}
    to {opacity:1;transform:translateY(0)}
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🛡️ TALASH AI")
    st.caption("SMART VISION & ANALYSIS")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Camera AI",
            "Activity Logs",
            "About Project"
        ]
    )

    st.divider()
    st.success("Interface Ready")
    st.caption("Academic Prototype v3.0")

# ================= HEADER =================
st.markdown("""
<div class="hero">
    <div class="hero-title">🛡️ TALASH AI</div>
    <div class="hero-sub">
        INTELLIGENT VISION • OBJECT DETECTION • TARA AI
    </div>
</div>
""", unsafe_allow_html=True)

st.caption(
    "TARA AI आपकी हिंदी Voice Assistant है। "
    "यह prototype सामान्य objects को पहचानने के लिए बनाया गया है।"
)

# ================= DASHBOARD =================
if page == "Dashboard":
    st.subheader("Welcome to TALASH AI")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="metric-label">SYSTEM</div>
            <div class="metric-value">🟢 READY</div>
            <p>Dashboard तैयार है</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="metric-label">VISION ENGINE</div>
            <div class="metric-value">👁️ AI</div>
            <p>Browser-based object detector</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="metric-label">VOICE ASSISTANT</div>
            <div class="metric-value">🎙️ TARA</div>
            <p>Hindi text-to-speech</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### ✨ TARA AI Assistant")

    components.html("""
    <html>
    <body style="margin:0;background:transparent;color:#e8f0ff;
                 font-family:Arial,sans-serif">
      <div style="display:flex;align-items:center;gap:16px;padding:18px;
                  border:1px solid #28566b;border-radius:18px;
                  background:linear-gradient(120deg,#102238,#10332f)">
        <div id="avatar" style="font-size:55px;border-radius:50%;
             background:#173650;padding:12px;
             animation:float 2s infinite">👩🏻‍💻</div>
        <div style="flex:1">
          <b style="font-size:21px;color:#54f5e5">TARA AI</b>
          <p id="msg" style="line-height:1.6">
            नमस्ते! मैं तारा हूँ, आपकी TALASH AI असिस्टेंट।
            Camera AI मोड में आप कैमरे से सामान्य वस्तुओं को पहचान सकते हैं।
          </p>
          <button onclick="speak()" style="padding:10px 14px;
             border:0;border-radius:9px;font-weight:bold;
             background:linear-gradient(90deg,#00d9f5,#00e6a0)">
             🔊 हिंदी में सुनें
          </button>
        </div>
      </div>
      <style>
        @keyframes float {
          0%,100%{transform:translateY(0)}
          50%{transform:translateY(-7px)}
        }
      </style>
      <script>
        function speak(){
          if(!('speechSynthesis' in window)) {
            alert('इस browser में voice उपलब्ध नहीं है।');
            return;
          }
          speechSynthesis.cancel();
          let u=new SpeechSynthesisUtterance(
            document.getElementById('msg').innerText
          );
          u.lang='hi-IN';u.rate=.9;u.pitch=1.1;
          let v=speechSynthesis.getVoices().find(
            x=>x.lang.toLowerCase().startsWith('hi')
          );
          if(v)u.voice=v;
          speechSynthesis.speak(u);
          document.getElementById('avatar').style.boxShadow=
            '0 0 25px #00e5ff';
          u.onend=()=>document.getElementById('avatar').style.boxShadow='none';
        }
      </script>
    </body>
    </html>
    """, height=180)

    st.markdown("### 🚀 मुख्य सुविधाएँ")
    st.markdown("""
    - 📷 Camera access और live preview
    - 🎯 Object के चारों ओर detection box
    - 📊 Confidence score
    - 🗣️ हिंदी में TARA AI voice
    - 📋 Detection results और session logs
    """)

# ================= CAMERA AI =================
elif page == "Camera AI":
    st.subheader("📷 Live Camera Object Detection")

    st.markdown("""
    <div class="note">
    <b>कैसे इस्तेमाल करें?</b><br>
    1. Start Camera दबाएँ।<br>
    2. Browser में camera permission Allow करें।<br>
    3. Camera के सामने कोई सामान्य वस्तु लाएँ।<br>
    4. AI पहचानी गई वस्तु का नाम और confidence दिखाएगा।
    </div>
    """, unsafe_allow_html=True)

    camera_html = r"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
    *{box-sizing:border-box}
    body{margin:0;background:#08111f;color:#eaf6ff;font-family:Arial}
    .wrap{padding:14px;border:1px solid #25455d;
          border-radius:18px;background:#0d1929}
    .top{display:flex;justify-content:space-between;gap:10px;
         flex-wrap:wrap;margin-bottom:12px}
    .brand{font-size:19px;font-weight:bold;color:#54f5e5}
    #status{font-size:12px;color:#00ffa3}
    .stage{position:relative;width:100%;background:#02060b;
           border-radius:12px;overflow:hidden;min-height:200px}
    video{display:block;width:100%;height:auto}
    canvas{position:absolute;left:0;top:0;width:100%;height:100%}
    .controls{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
    button{border:0;border-radius:10px;padding:11px 14px;
           font-weight:bold;cursor:pointer;
           background:linear-gradient(90deg,#00d9f5,#00e6a0);
           color:#06121b}
    button.stop{background:#26364b;color:white}
    button:disabled{opacity:.5;cursor:not-allowed}
    .result{margin-top:12px;border:1px solid #23465a;
            border-radius:12px;padding:13px;background:#101e30}
    #items{font-size:14px;line-height:1.8;color:#cde5f5}
    #hint{font-size:12px;line-height:1.6;color:#9fb4cd;margin-top:10px}
    </style>
    </head>
    <body>
    <div class="wrap">
      <div class="top">
        <div class="brand">◉ TARA VISION</div>
        <div id="status">● Camera बंद है</div>
      </div>
      <div class="stage">
        <video id="video" autoplay muted playsinline></video>
        <canvas id="canvas"></canvas>
      </div>
      <div class="controls">
        <button id="start">📷 Start Camera</button>
        <button id="stop" class="stop" disabled>■ Stop Camera</button>
        <button id="speak">🔊 हिंदी में बताओ</button>
      </div>
      <div class="result">
        <b>पहचानी गई वस्तुएँ</b>
        <div id="items">Camera चालू करके वस्तु दिखाएँ।</div>
        <div id="info" style="color:#91a9c5;font-size:12px;margin-top:8px">
          AI model load होने के लिए internet आवश्यक है।
        </div>
      </div>
      <div id="hint">
        Camera केवल Start Camera दबाने के बाद खुलेगा।
        पहचानी गई वस्तुओं के labels अनुमान हैं, अपराध का संकेत नहीं।
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.20.0/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd@2.2.3/dist/coco-ssd.min.js"></script>

    <script>
    const video=document.getElementById('video');
    const canvas=document.getElementById('canvas');
    const ctx=canvas.getContext('2d');
    const startBtn=document.getElementById('start');
    const stopBtn=document.getElementById('stop');
    const statusEl=document.getElementById('status');
    const itemsEl=document.getElementById('items');
    const info=document.getElementById('info');
    let stream=null,model=null,running=false,busy=false,latest=[];

    async function loadModel(){
      if(model)return model;
      info.textContent='AI model load हो रहा है...';
      if(!window.tf || !window.cocoSsd)
        throw new Error('Model library load नहीं हुई। Internet जाँचें।');
      await tf.ready();
      model=await cocoSsd.load();
      info.textContent='Model तैयार है। Camera शुरू हो सकता है।';
      return model;
    }

    function draw(predictions){
      if(!video.videoWidth)return;
      if(canvas.width!==video.videoWidth ||
         canvas.height!==video.videoHeight){
        canvas.width=video.videoWidth;
        canvas.height=video.videoHeight;
      }
      ctx.clearRect(0,0,canvas.width,canvas.height);
      ctx.lineWidth=Math.max(2,canvas.width/300);
      ctx.font='bold '+Math.max(14,canvas.width/38)+'px Arial';
      latest=predictions.filter(p=>p.score>=.45);

      latest.forEach(p=>{
        const [x,y,w,h]=p.bbox;
        ctx.strokeStyle='#00ffd0';
        ctx.shadowColor='#00e5ff';
        ctx.shadowBlur=8;
        ctx.strokeRect(x,y,w,h);
        ctx.shadowBlur=0;
        const label=p.class+' '+Math.round(p.score*100)+'%';
        const tw=ctx.measureText(label).width+12;
        const ly=Math.max(0,y-28);
        ctx.fillStyle='#00d9c0';
        ctx.fillRect(x,ly,tw,25);
        ctx.fillStyle='#03111a';
        ctx.fillText(label,x+6,ly+18);
      });

      if(latest.length){
        itemsEl.textContent=latest.map(p=>
          p.class+' ('+Math.round(p.score*100)+'%)'
        ).join(' · ');
        statusEl.textContent='● Object detected';
        statusEl.style.color='#00ffa3';
      } else {
        itemsEl.textContent='अभी कोई स्पष्ट वस्तु detect नहीं हुई।';
        statusEl.textContent='● Camera scanning';
        statusEl.style.color='#00e5ff';
      }
    }

    async function loop(){
      if(!running || busy)return;
      if(video.readyState>=2 && model){
        busy=true;
        try{
          const predictions=await model.detect(video);
          draw(predictions);
        }catch(e){
          info.textContent='Detection error: '+e.message;
        }
        busy=false;
      }
      if(running)requestAnimationFrame(loop);
    }

    startBtn.addEventListener('click',async()=>{
      startBtn.disabled=true;
      try{
        await loadModel();
        stream=await navigator.mediaDevices.getUserMedia({
          video:{facingMode:'environment'},audio:false
        });
        video.srcObject=stream;
        await video.play();
        running=true;
        stopBtn.disabled=false;
        statusEl.textContent='● Camera चालू है';
        info.textContent='Live object detection चालू है।';
        requestAnimationFrame(loop);
      }catch(e){
        statusEl.textContent='● Camera शुरू नहीं हुआ';
        statusEl.style.color='#ff8298';
        info.textContent='Error: '+e.message+
          '. Camera permission Allow करें और localhost इस्तेमाल करें।';
        startBtn.disabled=false;
      }
    });

    stopBtn.addEventListener('click',()=>{
      running=false;
      if(stream)stream.getTracks().forEach(t=>t.stop());
      stream=null;
      video.srcObject=null;
      ctx.clearRect(0,0,canvas.width,canvas.height);
      latest=[];
      itemsEl.textContent='Camera बंद है।';
      statusEl.textContent='● Camera बंद है';
      statusEl.style.color='#9fb4cd';
      stopBtn.disabled=true;
      startBtn.disabled=false;
    });

    document.getElementById('speak').addEventListener('click',()=>{
      if(!('speechSynthesis' in window)){
        info.textContent='इस browser में voice उपलब्ध नहीं है।';
        return;
      }
      const names=[...new Set(latest.map(p=>p.class))];
      const message=names.length
        ?'नमस्ते! तारा बता रही है। मुझे ये वस्तुएँ दिखाई दे रही हैं: '+names.join(', ')
        :'नमस्ते! अभी कोई स्पष्ट वस्तु detect नहीं हुई है।';
      speechSynthesis.cancel();
      const u=new SpeechSynthesisUtterance(message);
      u.lang='hi-IN';u.rate=.9;u.pitch=1.08;
      const voice=speechSynthesis.getVoices().find(
        v=>v.lang.toLowerCase().startsWith('hi')
      );
      if(voice)u.voice=voice;
      speechSynthesis.speak(u);
    });

    window.addEventListener('beforeunload',()=>{
      if(stream)stream.getTracks().forEach(t=>t.stop());
    });
    </script>
    </body>
    </html>
    """

    components.html(camera_html, height=680, scrolling=True)

# ================= ACTIVITY LOGS =================
elif page == "Activity Logs":
    st.subheader("📋 Activity Logs")
    st.info(
        "यह शुरुआती version live detections को Streamlit के logs में "
        "automatically save नहीं करता। Object detection browser में होता है।"
    )

    st.markdown("""
    <div class="card">
      <h3>कैमरा लॉग कैसे बढ़ाएँ?</h3>
      <p>अगले version में detections के नाम, समय और confidence को "
      "session history में save किया जा सकता है।</p>
    </div>
    """, unsafe_allow_html=True)

# ================= ABOUT =================
elif page == "About Project":
    st.subheader("🧠 About TALASH AI")

    st.markdown("""
    <div class="card">
      <h3>Project Overview</h3>
      <p>TALASH AI एक academic prototype है जो browser-based AI model
      की मदद से सामान्य objects पहचानता है।</p>
      <h3>Technology Stack</h3>
      <p>Python, Streamlit, HTML, CSS, JavaScript, TensorFlow.js और COCO-SSD</p>
      <h3>TARA AI</h3>
      <p>Browser की Hindi text-to-speech सुविधा से object labels सुनाए जा सकते हैं।</p>
      <h3>Limitations</h3>
      <p>यह व्यक्ति की पहचान नहीं करता और न ही किसी व्यक्ति को criminal
      घोषित कर सकता है। यह demo सामान्य वस्तुओं की पहचान तक सीमित है।</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown(
    "<p style='text-align:center;color:#71839c;font-size:12px'>"
    "TALASH AI • SMART VISION • ACADEMIC PROTOTYPE</p>",
    unsafe_allow_html=True
)
