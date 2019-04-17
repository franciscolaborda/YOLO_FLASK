from waitress import serve
import server_final
serve(server_final.app, host='0.0.0.0', port=8080)