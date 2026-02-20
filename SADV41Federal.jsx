import React, { useState, useEffect } from 'react';
import { Save, Plus, FileText, ShieldCheck } from 'lucide-react';

const FacturadorSADV41 = () => {
  const [facturas, setFacturas] = useState([]);
  const [form, setForm] = useState({
    cliente: '',
    servicio: 'Cambio de Neumáticos',
    monto: '',
    metodo: 'Efectivo',
    fecha: new Date().toISOString().split('T')[0]
  });

  // Cálculo del "Inyector de Crecimiento" (B/. 410.80 -> B/. 600)
  const totalGenerado = facturas.reduce((acc, curr) => acc + parseFloat(curr.monto || 0), 0);

  const manejarCambio = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const agregarFactura = (e) => {
    e.preventDefault();
    const nuevaFactura = { ...form, id: Date.now() };
    setFacturas([nuevaFactura, ...facturas]);
    setForm({ ...form, cliente: '', monto: '' });
    // Aquí se activaría la reacción en cadena hacia Google Sheets
    console.log("Factura registrada en la Misión SADV41:", nuevaFactura);
  };

  return (
    <div className="min-h-screen bg-black text-white p-4 font-sans">
      {/* Encabezado Federal */}
      <header className="max-w-4xl mx-auto border-b-2 border-yellow-600 pb-6 mb-8 text-center">
        <h1 className="text-3xl font-bold tracking-widest text-yellow-500 uppercase">
          🏛️ Sistema de Facturación Llantería Turbo Tire
        </h1>
        <p className="text-sm text-gray-400 mt-2 italic">
          Justificación de Productividad Federal - Repositorio StevenDiorFlow
        </p>
      </header>

      <main className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Formulario de Entrada */}
        <section className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800 shadow-2xl">
          <h2 className="flex items-center gap-2 text-xl font-semibold mb-6 text-yellow-500">
            <Plus size={24} /> Registrar Servicio
          </h2>
          <form onSubmit={agregarFactura} className="space-y-4
