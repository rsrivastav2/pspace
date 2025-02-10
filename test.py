 
      setData(result);
      setIsAuthorized(result.toLowerCase().includes("authorize")); // Check if "authorize" exists
    } catch (error) {
      console.error("Error fetching data:", error);
    }
