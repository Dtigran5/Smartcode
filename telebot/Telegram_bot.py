import telebot
import requests

# Replace with your actual Telegram bot token and Google API key
TELEGRAM_BOT_TOKEN = '7599131722:AAHD5uXzshuIPyvBFpJhTsAVGR2qdmC72LM'
GOOGLE_PLACES_API_KEY = 'AIzaSyADvgm_tYmO_8uE0II76D6Fa6HwRG4Ri04'

# Initialize bot
bot = telebot.TeleBot(token=TELEGRAM_BOT_TOKEN)

# Define categories
CATEGORIES = {
    'Fast Food': 'meal_takeaway',
    'Restaurant': 'restaurant',
    'Supermarket': 'supermarket',
    'Coffee Bar': 'cafe'
}

# Function to get nearby places
def get_nearby_places(lat, lon, category):
    places_type = CATEGORIES.get(category)
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=2000&type={places_type}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Check for errors in the API response
    if data.get("status") != "OK":
        return f"Error: {data.get('status')}. Please try again."
    
    results = data.get("results", [])
    
    # Build a detailed response for each place
    if not results:
        return "No places found nearby."
    
    places_info = []
    for place in results[:5]:  # Get top 5 places
        name = place.get('name')
        address = place.get('vicinity')
        rating = place.get('rating', 'No rating available')
        # Using HTML for formatting
        places_info.append(f"<b>{name}</b>\nAddress: {address}\nRating: {rating}/5\n")
    
    return "\n".join(places_info)

# Handle start command and send buttons
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for category in CATEGORIES.keys():
        markup.add(telebot.types.KeyboardButton(category))
    bot.send_message(message.chat.id, "Choose a category:", reply_markup=markup)

# Handle category buttons
@bot.message_handler(func=lambda message: message.text in CATEGORIES)
def send_places(message):
    category = message.text
    bot.send_message(message.chat.id, f"Please share your location or enter your coordinates for nearby {category} places.",
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    send_places.last_category = category  # Store the last selected category

# Handle location sharing
@bot.message_handler(content_types=['location'])
def location_handler(message):
    if hasattr(send_places, 'last_category'):
        category = send_places.last_category
        lat = message.location.latitude
        lon = message.location.longitude
        places_info = get_nearby_places(lat, lon, category)
        bot.send_message(message.chat.id, f"Nearby {category} places:\n\n{places_info}", parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Please select a category first.")

# Handle manual coordinates input
@bot.message_handler(func=lambda message: ',' in message.text)
def handle_lat_lon(message):
    try:
        lat, lon = map(float, message.text.split(','))
        category = getattr(send_places, 'last_category', None)
        if category:
            places_info = get_nearby_places(lat, lon, category)
            bot.send_message(message.chat.id, f"Nearby {category} places:\n\n{places_info}", parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, "Please select a category first.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid location in the format 'latitude, longitude' (e.g., '6.0, 1.0').")

# Start the bot
bot.polling()
