// Web App & Telegram Bot Integration
// This code will create a web page hosted on GitHub Pages and a Telegram bot with requested features

import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

const TELEGRAM_BOT_TOKEN = '7943104044:AAFUsDJHYfjHrkD0B4RbqPBZf6qnLWoTzKU';
const CHAT_ID = '6715819149';

// API URLs
const WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Hatikhuli,Kaziranga&appid=YOUR_API_KEY&units=metric';
const QUOTES_API_URL = 'https://type.fit/api/quotes';

const TelegramBotWebApp = () => {
  const [weather, setWeather] = useState(null);
  const [quote, setQuote] = useState('');
  const [isHindi, setIsHindi] = useState(false);

  useEffect(() => {
    fetchWeather();
    fetchQuote();
    runTelegramBot();
  }, []);

  const fetchWeather = async () => {
    try {
      const response = await fetch(WEATHER_API_URL);
      const data = await response.json();
      setWeather(data);
    } catch (error) {
      console.error('Error fetching weather:', error);
    }
  };

  const fetchQuote = async () => {
    try {
      const response = await fetch(QUOTES_API_URL);
      const data = await response.json();
      const randomQuote = data[Math.floor(Math.random() * data.length)];
      setQuote(randomQuote.text);
      setIsHindi(!isHindi);
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const runTelegramBot = () => {
    fetchWeather();
    fetchQuote();
    const message = `Weather: ${weather?.main?.temp}°C\nQuote: ${quote}`;
    sendMessageToTelegram(message);
  };

  const sendMessageToTelegram = async (message) => {
    const telegramApiUrl = `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`;
    try {
      await fetch(telegramApiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id: CHAT_ID, text: message })
      });
    } catch (error) {
      console.error('Error sending message to Telegram:', error);
    }
  };

  return (
    <div className="p-4">
      <Card className="mb-4">
        <CardContent>
          <h2 className="text-xl">Weather in Kaziranga, Hatikhuli</h2>
          {weather ? <p>{weather.main.temp}°C - {weather.weather[0].description}</p> : <p>Loading...</p>}
        </CardContent>
      </Card>

      <Card className="mb-4">
        <CardContent>
          <h2 className="text-xl">Motivational Quote</h2>
          <p>{quote}</p>
          <Button onClick={fetchQuote} className="mt-2">Get Another Quote</Button>
        </CardContent>
      </Card>
    </div>
  );
};

export default TelegramBotWebApp;
