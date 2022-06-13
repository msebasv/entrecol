import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'react-pro-sidebar/dist/css/styles.css'

import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Login from './pages/Login'
import Home from './pages/Home'
import Book from './pages/Book'
import Movie from './pages/Movie'
import Employee from './pages/Employee'
import GraphPage from './pages/GraphPage'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/book" element={<Book />} />
          <Route path="/movie" element={<Movie />} />
          <Route path="/employee" element={<Employee />} />
          <Route path="/graph" element={<GraphPage />} />
          <Route path="/" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
