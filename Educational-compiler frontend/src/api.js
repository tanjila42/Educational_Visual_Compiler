import axios from 'axios';

const API_URL = "http://localhost:5000"; // Backend URL

export const getCompilerData = async (input) => {
  try {
    const response = await axios.post(`${API_URL}/compiler_data`, { input }); // Send input code to backend
    return response.data; // Return data received from the backend
  } catch (error) {
    console.error('Error fetching data from backend:', error);
  }
};
