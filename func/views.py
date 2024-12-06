from django.shortcuts import redirect, render
from .models import Cart, CartEntry, Item

from openai import OpenAI

# Create your views here.
def menu(request):
    items = Item.objects.all()
    return render(request, 'func/menu.html', {'items': items})

def addToCart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart = Cart.objects.all().first()

    cartEntry = CartEntry.objects.filter(item=item, cart=cart).first()
    if cartEntry is None:
        cartEntry = CartEntry(item=item, cart=cart, quantity=1)
    else:
        cartEntry.quantity += 1
    cartEntry.save()

    return redirect('func:order')

def removeFromCart(request, cartEntryId):
    cartEntry = CartEntry.objects.get(pk=cartEntryId)
    cartEntry.delete()
    return redirect('func:cart')

def cart(request):
    cart = Cart.objects.all().first()
    cartEntries = CartEntry.objects.filter(cart=cart)

    token = "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"
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o-mini"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"I will give you the total Calories, Carbohydrates, Proteins and Fats of the items I am planning to eat in one single meal. I want you to give me advice on whether it is too high or too low in about 1 to 2 sentences. Calories: {cart.total_calories()}, Carbohydrates: {cart.total_carbs()}, Proteins: {cart.total_protein()}, Fats: {cart.total_fat()}",
            },
        ],
        model=model_name,
    )

    print(response.choices[0].message.content)

    return render(request, 'func/cart.html', {'cartEntries': cartEntries, 'cart': cart, 'advice': response.choices[0].message.content})