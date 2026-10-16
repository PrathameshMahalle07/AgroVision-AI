import React, { useState, useRef, useEffect } from 'react';
import {
  MessageSquare,
  Send,
  Sparkles,
  Bot,
  User,
  RefreshCw,
  Lightbulb,
} from 'lucide-react';
import { AssistantMessage, DiagnosisResultData, WeatherData } from '../types';
import { askCropAssistant } from '../services/aiAssistant';

interface AiCropAssistantProps {
  currentCrop: string;
  latestDiagnosis?: DiagnosisResultData | null;
  locationName: string;
  weather: WeatherData;
}

const SUGGESTED_QUESTIONS = [
  'Why are my leaves turning yellow?',
  "Will this week's rain affect my crop?",
  'How can I prevent this disease from spreading?',
  'What should I monitor over the next 7 days?',
];

export const AiCropAssistant: React.FC<AiCropAssistantProps> = ({
  currentCrop,
  latestDiagnosis,
  locationName,
  weather,
}) => {
  const [messages, setMessages] = useState<AssistantMessage[]>([
    {
      id: 'welcome',
      sender: 'assistant',
      text: `Hello! I'm your AgroVision crop-care advisor. I've loaded your current agronomic context: ${currentCrop}${
        latestDiagnosis?.condition ? ` with suspected ${latestDiagnosis.condition}` : ''
      } in ${locationName} (${weather.current.temp}°C, ${weather.current.humidity}% humidity). How can I assist you with your field management today?`,
      timestamp: 'Just now',
    },
  ]);
  const [inputQuestion, setInputQuestion] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const handleSend = async (questionText: string) => {
    const q = questionText.trim();
    if (!q || isTyping) return;

    const userMsg: AssistantMessage = {
      id: 'msg-' + Date.now(),
      sender: 'user',
      text: q,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputQuestion('');
    setIsTyping(true);

    try {
      const answer = await askCropAssistant(q, {
        crop: currentCrop,
        condition: latestDiagnosis?.condition,
        confidence: latestDiagnosis?.confidence,
        severity: latestDiagnosis?.severity,
        location: locationName,
        weather: {
          temp: weather.current.temp,
          humidity: weather.current.humidity,
          condition: weather.current.condition,
          forecastSummary: weather.forecast[0]?.condition,
        },
      });

      const assistantMsg: AssistantMessage = {
        id: 'msg-res-' + Date.now(),
        sender: 'assistant',
        text: answer,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err: any) {
      const errorMsg: AssistantMessage = {
        id: 'msg-err-' + Date.now(),
        sender: 'assistant',
        text: 'Sorry, I encountered an issue retrieving an answer. Please verify your connection or try again.',
        timestamp: 'Just now',
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl border border-[#DFE7DF] shadow-md overflow-hidden flex flex-col h-[520px]">
      {/* Assistant Header */}
      <div className="p-4 sm:p-5 bg-[#F8FAF7] border-b border-[#E8EDE8] flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-[#234E35] text-white flex items-center justify-center shadow-xs">
            <Sparkles className="w-4 h-4 text-[#8CE39B]" />
          </div>
          <div>
            <h4 className="text-sm font-serif font-bold text-[#142C1F] flex items-center gap-1.5">
              Ask About Your Crop
              <span className="text-[10px] font-sans font-semibold px-2 py-0.2 rounded-full bg-[#E5EFE7] text-[#245437]">
                Context-Aware
              </span>
            </h4>
            <p className="text-[11px] text-[#637568]">
              Grounding in {currentCrop}, local weather & recent scan data
            </p>
          </div>
        </div>

        <div className="hidden sm:flex items-center gap-1 text-[11px] text-[#4E6153] bg-white px-2.5 py-1 rounded-lg border border-[#DDE7DE]">
          <span>{locationName}</span>
          <span>•</span>
          <span>{weather.current.temp}°C</span>
        </div>
      </div>

      {/* Messages Thread */}
      <div className="flex-1 p-4 overflow-y-auto space-y-3.5 bg-[#FAFBF9]">
        {messages.map((msg) => {
          const isUser = msg.sender === 'user';
          return (
            <div
              key={msg.id}
              className={`flex items-start gap-2.5 ${isUser ? 'flex-row-reverse' : ''}`}
            >
              <div
                className={`w-7 h-7 rounded-full flex items-center justify-center shrink-0 text-xs font-semibold ${
                  isUser
                    ? 'bg-[#234E35] text-white'
                    : 'bg-[#E5EFE7] text-[#234E35] border border-[#CCDCD0]'
                }`}
              >
                {isUser ? <User className="w-3.5 h-3.5" /> : <Bot className="w-3.5 h-3.5" />}
              </div>

              <div
                className={`max-w-[85%] sm:max-w-[78%] rounded-2xl p-3 text-xs leading-relaxed ${
                  isUser
                    ? 'bg-[#234E35] text-white rounded-tr-xs shadow-xs'
                    : 'bg-white text-[#203125] border border-[#E3ECE4] rounded-tl-xs shadow-2xs'
                }`}
              >
                <p className="whitespace-pre-line">{msg.text}</p>
                <span
                  className={`text-[9px] block mt-1 ${
                    isUser ? 'text-[#BFD8C5] text-right' : 'text-[#87998B]'
                  }`}
                >
                  {msg.timestamp}
                </span>
              </div>
            </div>
          );
        })}

        {isTyping && (
          <div className="flex items-center gap-2 text-xs text-[#637568] p-2 bg-white rounded-xl border border-[#E3ECE4] max-w-fit">
            <RefreshCw className="w-3.5 h-3.5 animate-spin text-[#234E35]" />
            <span>Consulting agronomic knowledge base...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Suggested Questions Chips */}
      <div className="px-4 py-2 bg-[#F3F7F4] border-t border-[#E8EDE8] flex items-center gap-1.5 overflow-x-auto">
        <Lightbulb className="w-3.5 h-3.5 text-[#376949] shrink-0" />
        <span className="text-[10px] uppercase font-bold text-[#4B6051] shrink-0">
          Suggestions:
        </span>
        {SUGGESTED_QUESTIONS.map((q, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => handleSend(q)}
            disabled={isTyping}
            className="text-[11px] px-2.5 py-1 rounded-lg bg-white border border-[#D5E1D7] text-[#2F4435] hover:bg-[#EBF2EC] transition whitespace-nowrap shrink-0 cursor-pointer disabled:opacity-50"
          >
            {q}
          </button>
        ))}
      </div>

      {/* Input Field */}
      <div className="p-3 bg-white border-t border-[#E8EDE8]">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend(inputQuestion);
          }}
          className="flex items-center gap-2"
        >
          <input
            type="text"
            placeholder={`Ask a question about your ${currentCrop}...`}
            value={inputQuestion}
            onChange={(e) => setInputQuestion(e.target.value)}
            disabled={isTyping}
            className="flex-1 text-xs py-2.5 px-3.5 border border-[#D5E0D6] rounded-xl focus:outline-none focus:border-[#234E35] focus:ring-1 focus:ring-[#234E35]/20 bg-[#FAFBF9]"
          />
          <button
            type="submit"
            disabled={!inputQuestion.trim() || isTyping}
            className="p-2.5 rounded-xl bg-[#234E35] hover:bg-[#1A3D29] text-white transition disabled:opacity-50 cursor-pointer"
            aria-label="Send question"
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  );
};
