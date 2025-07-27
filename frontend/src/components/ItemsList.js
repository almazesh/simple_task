import React, { useState, useEffect } from 'react';

const ItemsList = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newCaption, setNewCaption] = useState('');

  // URL API (можно изменить на любой)
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  // Загрузка данных с сервера
  const fetchItems = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/api/items`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setItems(data.items || []);
      setError(null);
    } catch (err) {
      console.error('Error fetching items:', err);
      setError('Ошибка загрузки данных: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Создание новой записи
  const createItem = async () => {
    if (!newCaption.trim()) {
      alert('Пожалуйста, введите текст');
      return;
    }

    try {
      const response = await fetch(`${API_URL}/api/items`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ caption: newCaption }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      setNewCaption('');
      await fetchItems(); // Перезагружаем список
    } catch (err) {
      console.error('Error creating item:', err);
      setError('Ошибка создания записи: ' + err.message);
    }
  };

  // Удаление записи
  const deleteItem = async (id) => {
    if (!window.confirm('Удалить эту запись?')) {
      return;
    }

    try {
      const response = await fetch(`${API_URL}/api/items/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      await fetchItems(); // Перезагружаем список
    } catch (err) {
      console.error('Error deleting item:', err);
      setError('Ошибка удаления записи: ' + err.message);
    }
  };

  // Загрузка данных при монтировании компонента
  useEffect(() => {
    fetchItems();
  }, []);

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Загрузка данных...</p>
      </div>
    );
  }

  return (
    <div className="items-container">
      <h2>📋 Список записей из PostgreSQL</h2>
      
      {error && (
        <div className="error-message">
          ❌ {error}
          <button onClick={fetchItems} className="retry-btn">
            🔄 Повторить
          </button>
        </div>
      )}

      {/* Форма добавления новой записи */}
      <div className="add-item-form">
        <h3>➕ Добавить новую запись</h3>
        <div className="input-group">
          <input
            type="text"
            value={newCaption}
            onChange={(e) => setNewCaption(e.target.value)}
            placeholder="Введите текст записи..."
            className="caption-input"
            onKeyPress={(e) => e.key === 'Enter' && createItem()}
          />
          <button onClick={createItem} className="add-btn">
            Добавить
          </button>
        </div>
      </div>

      {/* Статистика */}
      <div className="stats">
        <p>📊 Всего записей: <strong>{items.length}</strong></p>
        <button onClick={fetchItems} className="refresh-btn">
          🔄 Обновить
        </button>
      </div>

      {/* Список записей */}
      {items.length === 0 ? (
        <div className="no-items">
          <p>📝 Записей пока нет</p>
        </div>
      ) : (
        <div className="items-grid">
          {items.map((item) => (
            <div key={item.id} className="item-card">
              <div className="item-header">
                <span className="item-id">ID: {item.id}</span>
                <button 
                  onClick={() => deleteItem(item.id)}
                  className="delete-btn"
                  title="Удалить запись"
                >
                  🗑️
                </button>
              </div>
              <div className="item-caption">
                <strong>Caption:</strong> {item.caption}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ItemsList;
