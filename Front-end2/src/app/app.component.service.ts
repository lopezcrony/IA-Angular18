import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:5000/chat';  // Cambia esto a la URL de tu backend con la IA

  constructor(private http: HttpClient) { }

  // Método para enviar el mensaje del usuario al backend y obtener la respuesta
  sendMessage(message: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}`, { prompt: message });
  }
}