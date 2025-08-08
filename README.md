# 🧠 MindCare AI Assistant

A compassionate AI-powered mental health support system featuring Dr. Emily, a virtual clinical psychologist designed to provide empathetic, evidence-based therapeutic guidance.

## 🌟 Features

### **Therapeutic AI Assistant**
- **Dr. Emily**: A warm, professional AI therapist with 15+ years of clinical experience
- **Evidence-Based Approach**: Grounded in cognitive-behavioral therapy (CBT) and mindfulness practices
- **Crisis Management**: Built-in safety protocols for mental health emergencies
- **Personalized Support**: Tailored responses based on individual needs and concerns

### **Technical Capabilities**
- **Real-time Chat Interface**: Streamlit-based web application
- **Advanced AI Integration**: Powered by Google's Gemini 2.5 Flash model
- **Emergency Response System**: Twilio integration for crisis situations
- **Therapist Locator**: Find nearby mental health professionals
- **Session Management**: Persistent conversation history and context

## 🏗️ Architecture

```
MindCare AI Assistant/
├── frontend.py              # Streamlit web interface
├── backend/
│   ├── main.py             # FastAPI server
│   ├── agent.py            # LangChain agent setup
│   ├── tools.py            # AI tools and Dr. Emily implementation
│   └── config.py           # API keys and configuration
├── dr_emily_system_instructions.md  # AI personality guidelines
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Twilio account (for emergency features)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mindcare-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit fastapi uvicorn google-generativeai twilio langchain langgraph langchain-google-genai
   ```

3. **Configure API keys**
   ```bash
   # Edit backend/config.py
   GEMINI_API_KEY = "your-gemini-api-key"
   TWILIO_ACCOUNT_SID = "your-twilio-sid"
   TWILIO_AUTH_TOKEN = "your-twilio-token"
   TWILIO_FROM_NUMBER = "your-twilio-number"
   TWILIO_TO_NUMBER = "emergency-contact"
   ```

4. **Start the backend server**
   ```bash
   cd backend
   python main.py
   ```

5. **Launch the frontend**
   ```bash
   streamlit run frontend.py
   ```

6. **Access the application**
   - Open your browser to `http://localhost:8501`
   - Start chatting with Dr. Emily!

## 🧠 Dr. Emily - AI Therapist

### **Professional Profile**
- **Name**: Dr. Emily Hartman
- **Specialization**: Clinical Psychology (CBT, Mindfulness, Trauma-Informed Care)
- **Experience**: 15+ years in clinical practice
- **Approach**: Warm, empathetic, and evidence-based

### **Therapeutic Techniques**
- **Cognitive-Behavioral Therapy (CBT)**: Identify and challenge unhelpful thought patterns
- **Mindfulness Practices**: Present-moment awareness and grounding techniques
- **Solution-Focused Therapy**: Build on strengths and resources
- **Crisis Intervention**: Immediate safety protocols and referrals

### **Safety Features**
- **Crisis Detection**: Automatic identification of suicidal thoughts or self-harm
- **Emergency Response**: Direct connection to crisis hotlines
- **Professional Boundaries**: Clear scope of practice and referral guidelines
- **24/7 Availability**: Round-the-clock mental health support

## 🛠️ Technical Stack

### **Frontend**
- **Streamlit**: Interactive web interface
- **Real-time Chat**: Persistent conversation history
- **Responsive Design**: Mobile-friendly interface

### **Backend**
- **FastAPI**: High-performance API server
- **LangChain**: AI agent framework
- **Google Gemini**: Advanced language model
- **Twilio**: Emergency communication system

### **AI/ML**
- **Gemini 2.5 Flash**: State-of-the-art language model
- **Custom System Prompts**: Tailored therapeutic personality
- **Context Management**: Persistent conversation memory
- **Tool Integration**: Specialized mental health tools

## 🔧 Configuration

### **Environment Variables**
```python
# backend/config.py
GEMINI_API_KEY = "your-api-key"
TWILIO_ACCOUNT_SID = "your-sid"
TWILIO_AUTH_TOKEN = "your-token"
TWILIO_FROM_NUMBER = "your-number"
TWILIO_TO_NUMBER = "emergency-number"
```

### **Model Configuration**
- **Model**: `gemini-2.5-flash`
- **Temperature**: 0.2 (balanced creativity and consistency)
- **System Instructions**: Comprehensive therapeutic guidelines
- **Safety Protocols**: Built-in crisis management

## 🚨 Safety & Ethics

### **Crisis Management**
- **Immediate Response**: Automatic crisis detection and intervention
- **Emergency Contacts**: Direct connection to suicide prevention hotlines
- **Professional Referrals**: Local therapist and mental health resource locator
- **Safety First**: Always prioritize user safety and well-being

### **Professional Boundaries**
- **No Medical Advice**: Does not provide medication recommendations
- **No Formal Diagnosis**: Offers support, not clinical diagnosis
- **Referral System**: Connects users to licensed professionals
- **Confidentiality**: Clear data handling and privacy policies

### **Ethical Guidelines**
- **Informed Consent**: Clear communication about AI capabilities
- **Scope Limitations**: Transparent about therapeutic boundaries
- **Crisis Protocols**: Immediate escalation for safety concerns
- **Professional Standards**: Adherence to mental health best practices

## 📊 Usage Examples

### **General Support**
```
User: "I'm feeling anxious about my job interview tomorrow."
Dr. Emily: "I hear how challenging this situation is for you. Let's explore what's contributing to these feelings and work on some grounding techniques together."
```

### **Crisis Intervention**
```
User: "I don't think I can go on anymore."
Dr. Emily: "I'm concerned about your safety. Please contact the National Suicide Prevention Lifeline at 988 immediately, or go to your nearest emergency room."
```

### **Therapist Referral**
```
User: "I need to find a therapist in New York."
Dr. Emily: "I can help you locate mental health professionals in your area. Let me search for licensed therapists near you."
```

## 🔄 API Endpoints

### **POST /ask**
- **Purpose**: Process user messages and generate therapeutic responses
- **Input**: `{"message": "user message"}`
- **Output**: `{"response": "therapeutic response", "tool_called": "tool_name"}`

### **Response Format**
```json
{
  "response": "Dr. Emily's therapeutic response",
  "tool_called": "ask_mental_health_specialist"
}
```

## 🛡️ Security & Privacy

### **Data Protection**
- **No Persistent Storage**: Conversations are not permanently stored
- **Session-based**: Data cleared when browser session ends
- **API Security**: Secure transmission of all communications
- **Privacy First**: Minimal data collection and processing

### **Access Control**
- **No Authentication Required**: Immediate access for crisis situations
- **Anonymous Support**: No personal information required
- **Safe Environment**: Non-judgmental, supportive space

## 🤝 Contributing

We welcome contributions to improve MindCare AI Assistant!

### **Development Guidelines**
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### **Areas for Contribution**
- **Enhanced Crisis Detection**: Improve safety protocols
- **Additional Therapeutic Tools**: Expand AI capabilities
- **UI/UX Improvements**: Better user experience
- **Documentation**: Clearer guides and examples
- **Testing**: Comprehensive test coverage

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**Important**: MindCare AI Assistant is designed to provide mental health support and is not a replacement for professional medical care. 

- **Not a Substitute**: This AI does not replace licensed mental health professionals
- **Crisis Situations**: Always contact emergency services for immediate crisis situations
- **Professional Care**: Seek professional help for serious mental health concerns
- **Emergency Use**: Call 988 (Suicide Prevention Lifeline) or 911 for emergencies

## 📞 Emergency Resources

- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **Emergency Services**: 911
- **Local Mental Health Resources**: Contact your healthcare provider

## 🙏 Acknowledgments

- **Google Gemini**: Advanced AI language model
- **Streamlit**: Interactive web framework
- **FastAPI**: High-performance API framework
- **Mental Health Community**: Ongoing support and feedback
- **Open Source Community**: Contributing to mental health technology

---

**Built with ❤️ for mental health support and wellness**

*MindCare AI Assistant - Supporting mental wellness through compassionate AI technology*
