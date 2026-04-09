import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet, TouchableOpacity } from 'react-native';

export default function ProductManager() {
  const [productName, setProductName] = useState('');
  const [products, setProducts] = useState([]);
  const [evaluations, setEvaluations] = useState([]);

  // إضافة منتج جديد
  const addProduct = () => {
    if (productName.trim() === '') return;
    const newProduct = {
      id: Date.now().toString(),
      name: productName,
      rating: 0, // يبدأ بدون تقييم
    };
    setProducts([...products, newProduct]);
    setEvaluations([...evaluations, `Saden أضاف المنتج: ${productName}`]);
    setProductName('');
  };

  // تقييم منتج بالنجوم
  const rateProduct = (id, rating) => {
    const updatedProducts = products.map((p) =>
      p.id === id ? { ...p, rating } : p
    );
    setProducts(updatedProducts);
    const product = updatedProducts.find((p) => p.id === id);
    setEvaluations([...evaluations, `Saden قيّم ${product.name} بـ ${rating} نجوم`]);
  };

  // عرض النجوم للتقييم
  const renderStars = (id, currentRating) => {
    return (
      <View style={{ flexDirection: 'row' }}>
        {[1, 2, 3, 4, 5].map((star) => (
          <TouchableOpacity key={star} onPress={() => rateProduct(id, star)}>
            <Text style={{ fontSize: 20, color: star <= currentRating ? 'gold' : 'gray' }}>
              ★
            </Text>
          </TouchableOpacity>
        ))}
      </View>
    );
  };

  // حساب متوسط التقييم العام
  const averageRating = products.length > 0
    ? (products.reduce((sum, p) => sum + p.rating, 0) / products.length).toFixed(1)
    : 0;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>⭐ FlashDeal Star - منتجاتي ⭐</Text>
      
      <TextInput
        style={styles.input}
        placeholder="أدخل اسم المنتج"
        value={productName}
        onChangeText={setProductName}
      />
      
      <Button title="➕ أضف المنتج" onPress={addProduct} />

      <Text style={styles.sectionTitle}>📊 متوسط التقييم العام: {averageRating} / 5 ⭐</Text>

      <Text style={styles.sectionTitle}>📱 قائمة المنتجات:</Text>
      <FlatList
        data={products}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{ marginVertical: 5 }}>
            <Text style={styles.productItem}>- {item.name}</Text>
            {renderStars(item.id, item.rating)}
          </View>
        )}
      />

      <Text style={styles.sectionTitle}>📝 سجل التقييمات:</Text>
      <FlatList
        data={evaluations}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <Text style={styles.evaluationItem}>{item}</Text>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, marginTop: 40 },
  title: { fontSize: 20, fontWeight: 'bold', marginBottom: 10 },
  input: { borderWidth: 1, borderColor: '#ccc', padding: 10, marginBottom: 10 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginTop: 20 },
  productItem: { fontSize: 16 },
  evaluationItem: { fontSize: 14, color: '#555', marginVertical: 3 }
});
